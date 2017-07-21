#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root" 1>&2
	exit 1
fi

while getopts ":lu" opt; do
	case $opt in
		l)
			modprobe w1-gpio gpiopin=4
			if [ "$?" -ne 0 ]; then echo "Failed to load w1-gpio"; exit 1; fi

			modprobe w1-ds2433
			if [ "$?" -ne 0 ]; then echo "Failed to load w1-ds2433"; exit 1; fi
			echo "Successfully loaded w1-gpio & w1-ds2433 kernel modules"
			exit 1
		;;
		u)
			rmmod w1-gpio
			if [ "$?" -ne 0 ]; then echo "Failed to unload w1-gpio"; exit 1; fi

			rmmod w1-ds2433
			if [ "$?" -ne 0 ]; then echo "Failed to unload w1-ds2433"; exit 1; fi
			echo "Successfully unloaded w1-gpio & w1-ds2433 kernel modules"
			exit 1
		;;
		\?)
			echo "Invalid option: -$OPTARG" >&2
		exit 1
		;;
  esac
done
