#! /bin/bash
FILE=./build_text
BUILD_TEXT="$(grep "BUILD_ID" $FILE)"
sed -i.bak -e "s/.*BUILD_ID=.*/BUILD_ID=$((${BUILD_TEXT##*=}+1))/" $FILE
