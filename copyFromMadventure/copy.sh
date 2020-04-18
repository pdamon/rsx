#!/bin/bash

echo "Copying files " /pi/media/*/*.jpg "To current directory"
cp /pi/media/*/*.jpg .

if [ $? == 0 ]
then
	echo "Copying Complete"
	exit 0
else
	echo "Errors Occured"
	echo "Exiting with Code 1"
	exit 1
fi
