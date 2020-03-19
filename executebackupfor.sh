#!/bin/bash

eval para1="$1"
eval para2="$2"

if [ ${#para1} -ne 6 ]; then
    echo "Invalid Starting Period"
    exit 0
elif [ ${#para2} -ne 6 ]; then
    echo "Invalid Ending Period"
    exit 0
elif [ ${para2} -lt ${para1} ]; then
    echo "Invalid Period Range"
    exit 0
fi

cd ~

if [ -e ~/executedatabasebackup.sh ]; then
    rm ~/executedatabasebackup.sh
    touch ~/executedatabasebackup.sh
fi

databaseLine=""
monthToProcess=${para1:(-2)}
yearToProcess=${para1:0:4}
monthToProcess=$(printf "%02d" $monthToProcess)
monthToProcess2=${para2:(-2)}
monthToProcess2=$(printf "%02d" $monthToProcess2)

if [ $monthToProcess -gt 12 ]; then
    echo "Invalid Input for Month "
    exit 0
fi

if [ $monthToProcess2 -gt 12 ]; then
    echo "Invalid Input for Month "
    exit 0
fi

for (( i = ${para1}; i <= ${para2}; i++)); do
    monthToProcess=$(printf "%02d" $monthToProcess)
    databaseToBackup=$yearToProcess$monthToProcess
    if [ $databaseToBackup -gt ${para2} ]; then
        break
    fi
    databaseLine=$databaseLine" db"$databaseToBackup
    monthToProcess=`expr $monthToProcess + 1`
    if [ $monthToProcess -ge 13 ];then
        monthToProcess=01
        yearToProcess=`expr $yearToProcess + 1`
    fi
done

databaseLine=$databaseLine" forapproval genesys_accountcharts master par"
commandInScript="mysql -u sysad -h 127.0.0.1 -p --skip-set-charset --add-drop-database --databases "$databaseLine

echo $commandInScript >> executedatabasebackup.sh 

chmod +x executedatabasebackup.sh
./executedatabasebackup.sh

