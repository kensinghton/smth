#!/bin/bash
title="$1"  #title='Blacklist'
sType="$2"  #sType='1080p'
[[ $title == '' || $sType == '' ]] && exit 1
sUID='2803673'
sUSESS='30a367747c0fade5c243df58128e4943'
wget -q retre.org/rssdd.xml
titles=$(grep -A 3 "$title" rssdd.xml)
titleTYPE=$(echo "$titles" | grep -A 2 "$sType" | tail -1 | xargs)
sLink="${titleTYPE:6:-8}"
titleFILE=$(echo "$titles" | grep -B 1 "$sType" | head -2 | tail -1 | xargs)
sFileNumber=$(echo "${titleFILE:7:-9}" | grep -o "S..E..")
wget -q "$sLink" --header "Cookie: uid=$sUID;usess=$sUSESS" -O "$HOME/.transmission/rssfeed/${title}_${sFileNumber}.torrent"
rm -f rssdd.xml* rssdownloader*