#!/bin/bash
#get filemask from nomad/ directory
#parse files for "true"
#when got 2 "true" stop
#
FULLNAME=$(ls nomad/*.log|head -1)
FILEMASK=${FULLNAME##*/}
FILEMASK2=${FILEMASK//[0-9]/}
