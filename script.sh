#!/bin/bash
#get filemask from nomad/ directory
#parse files for "true"
#when got 2 "true" stop
#
FULLNAME=$(ls nomad/*.log|head -1)
FILEMASK=${FULLNAME##*/}
FILEMASK2=${FILEMASK//[0-9]/}

FN=$(ls nomad/|head -1)
FM=${FN##*/}
FM2=$(FM//[0-9]/}
FN=${FM2::-4}
echo $FN
