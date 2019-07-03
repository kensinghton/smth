#!/bin/bash
DIRNAME=log
F1=$(ls $DIRNAME|head -1)
F2=${F1//[0-9]/}
FILENUM=$(ls -1 $DIRNAME | wc -l)
TRUENUM=0
for i in $(seq 1 $FILENUM); do
        if [ $(cat ./$DIRNAME/$F2$i) = 'true' ]; then
          TRUENUM=$(($TRUENUM+1))
                if [ $TRUENUM = 2 ]; then break 2 
                fi
         fi
done 
echo "$i was final"
