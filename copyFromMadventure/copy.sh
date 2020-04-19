# run this script with ./copy.sh
#
#!/bin/bash

MADPATH="/pi/media/*/DCIM/*/*.JPG"
echo "Copying files " ${MADPATH} "To current directory"
cp ${MADPATH} .

if [ $? == 0 ]
then
	echo "Copying Complete"
	exit 0
else
	echo "Errors Occured"
	echo "Exiting with Code 1"
	exit 1
fi
