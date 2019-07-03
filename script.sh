 1 #!/bin/bash
 2 DIRNAME=log
 3 F1=$(ls $DIRNAME|head -1)
 4 F2=${F1##*/}
 5 F3=${F2//[0-9]/}
 6 echo $F3
 7 FILENUM=$(ls -1 $DIRNAME | wc -l)
 8 TRUENUM=0
 9 while [[ $TRUENUM = '2' ]]; do
10  for i in {1..$FILENUM}; do
11         if [ `$(cat $F3$i)` == 'true' ; ]; then
12           TRUENUM=$TRUENUM+1
13           echo $TRUENUM
14         fi
15  done
16 done
17
18 echo "$TRUENUM is done"
