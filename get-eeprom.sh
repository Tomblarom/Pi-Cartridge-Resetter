#!/bin/bash

W1_DIR="/sys/bus/w1/devices/w1_bus_master1"
tmpDir="/tmp/eepromWriter"

dirs=$W1_DIR/23-*/
missingEeprom=true
for dir in $dirs
do
		if [ -d $dir ]; then
		(( itterationCount++ ))
		{
			cp $dir"eeprom" "/tmp/test.bin"
		} && {
		{
			missingEeprom=false
			{
				eepromID=$(xxd -p $dir"id")
			} && {
				if [ -d $tmpDir ]; then
					rm -rf $tmpDir
				fi
				mkdir $tmpDir
		
				echo "$eepromID" > $tmpDir/uid
				(dd conv=swab < $tmpDir/uid > $tmpDir/swab_uid) > /dev/null 2>&1
				swabID=$(cat $tmpDir/swab_uid)
				revID=$(echo $swabID|rev)
				echo "$revID" > $tmpDir/rev_uid
		
				binaryName="original-"$eepromID".bin"
				{
					cp $dir"eeprom" $tmpDir"/"$binaryName
				} || {
					missingEeprom=true
				}
			}
		} || {
			missingEeprom=true
		}
		}
	fi
done

if [ "$missingEeprom" = true ]; then
	echo "No EEPROM found."
	if [ -d $tmpDir ]; then
		rm -rf $tmpDir
	fi
else
    ls /tmp/eepromWriter
fi
