#!/bin/bash

#prep
mkdir ~/tmp
cd ~/tmp

#chrome
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | \
sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ \
stable main" >> /etc/apt/sources.list.d/google.list'

#telegram
sudo add-apt-repository ppa:atareao/telegram -y

#scribus
sudo add-apt-repository ppa:scribus/ppa -y

#add multiverse
sudo add-apt-repository multiverse -y

#slack
wget https://downloads.slack-edge.com/linux_releases/slack-desktop-4.0.2-amd64.deb

#zoom
wget https://zoom.us/client/latest/zoom_amd64.deb

#megamekhq
wget https://github.com/MegaMek/mekhq/releases/download/v0.47.5/mekhq-0.47.5.tar.gz
mkdir ~/games
tar -xf mekhq-0.47.5.tar.gz
cat >~/.local/share/applications/mekhq.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=MekHQ
Comment=
Path=/home/axeller/games/mekhq-0.47.5/
Exec=bash ./hq
Icon=/home/axeller/games/mekhq-0.47.5/data/images/misc/mekhq.png
Terminal=false
Type=Application
EOF

#minecraft
sudo dpkg --add-architecture i386
wget -O - https://mcpelauncher.mrarm.io/apt/conf/public.gpg.key | sudo apt-key add -
sudo add-apt-repository 'deb http://mcpelauncher.mrarm.io/apt/ubuntu/ bionic main' -y

#default
apt update && apt upgrade -y
apt install -y nano vagrant google-chrome-stable vlc gnome-tweaks \
               kdeconnect gimp inkscape telegram scribus-ng steam \
               openjdk-8-jdk msa-daemon msa-ui-qt mcpelauncher-client \
               mcpelauncher-ui-qt libegl1-mesa:i386 libegl1-mesa-dev:i386 \
               chrome-gnome-shell
sudo apt install ./slack-desktop-*.deb ./zoom_amd64.deb -y
