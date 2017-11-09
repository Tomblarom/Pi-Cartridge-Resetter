#!/usr/bin/python
import os, subprocess, os.path, time
import Adafruit_CharLCD as LCD

# subprocess.call("./modules.sh -l", shell=True)
# subprocess.call("./get-eeprom.sh", shell=True)

# tmpDir="/tmp/eepromWriter"
# stratDir="/opt/eepromTool/stratasys-master"
# if not os.path.isdir(tmpDir):
#	print "No EEPROM found."
# else:
#	printerType="prodigy"
#	revID=open(tmpDir+"/rev_uid")
#	revID=revID.read().strip('\n')
#	eepromID=open(tmpDir+"/uid")
#	eepromID=eepromID.read().strip('\n')
#	os.system(stratDir+'/stratasys-cli.py eeprom -t '+printerType+' -e '+revID+' -i '+tmpDir+'/original-'+eepromID+'.bin')

# subprocess.call("./modules.sh -u", shell=True)

lcd = LCD.Adafruit_CharLCDPlate()
lcd.create_char(1, [6, 10, 16, 30, 17, 17, 17, 14])
lcd.create_char(2, [12, 10, 1, 15, 17, 17, 17, 14])
lcd.create_char(3, [0, 0, 17, 27, 31, 31, 14, 4])
lcd.create_char(4, [0, 14, 14, 14, 14, 14, 10, 4])
lcd.create_char(5, [10, 14, 4, 4, 14, 14, 14, 14])
lcd.create_char(6, [28, 16, 28, 8, 8, 8, 8, 8])

lcd.clear()

# Selection in menu
state = 0

# 0: Menu
# 1: Submenu
layer = 0

# Selction in Submenu
select = 0

update = True

states = (('\x01\x02 Read Chip', (0, 1, 0)),
          ('\x03\x04 Write Chip', (1, 0, 0)),
          ('\x05\x06 Extras', (0, 1, 1)))

selects_1 = ((''),
             (''),
             (''))

selects_2 = (('Profiles'),
             ('New Profile'))

selects_3 = ((''),
             (''),
             (''))

selects = (selects_1,
          selects_2,
          selects_3)


def output(text, r, g, b):
    lcd.clear()
    lcd.message(text, )
    lcd.set_color(r, g, b)


while True:
    if layer == 0:
        if lcd.is_pressed(LCD.SELECT):
            layer = 1
            time.sleep(0.17)
            update = True

        if lcd.is_pressed(LCD.LEFT):
            if state == 0:
                state = 2
            elif state == 1:
                state = 0
            elif state == 2:
                state = 1
            time.sleep(0.17)
            update = True

        if lcd.is_pressed(LCD.LEFT):
            if state == 0:
                state = 2
            elif state == 1:
                state = 0
            elif state == 2:
                state = 1
            time.sleep(0.17)
            update = True

        if lcd.is_pressed(LCD.RIGHT):
            if state == 0:
                state = 1
            elif state == 1:
                state = 2
            elif state == 2:
                state = 0
            time.sleep(0.17)
            update = True

        for idx, statev in enumerate(states):
            if idx == state and update:
                output(statev[0], statev[1][0], statev[1][1], statev[1][2])
                update = False

    if layer == 1:

        if state == 0:
            # Read Chip
            print()
        elif state == 1:
            print()
        elif state == 2:
            # Settings
            print()

        for idx, selectv in enumerate(selects):
            if idx == state and update:
                output(selectv[0]+'\n'+selectv[1], 1, 1, 1)
                update = False

        if lcd.is_pressed(LCD.UP):
            layer = 0
            time.sleep(0.17)
            update = True
