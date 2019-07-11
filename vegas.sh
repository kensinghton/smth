#!/bin/bash
cash=100
dice_check='^[1-6]+$'
cheater=''
message=''
clear
echo "Welcome to fabulous Vegas.sh!\nLets play Dice!\nYou got $cash$\nEnter your name:"
read player
while : 
do 
        if [ "$cash" -le "0" ]; 
        then echo "$player, you got no money, get out of here!\nYou got $cash$."; 
                break 2 
        else
                clear
                echo "$message\n"
                echo "You got $cash$.\n $player, please type number between 1 and 6,\n or type 'quit' to leave, or 'add' or 'rem' for... something:"
                read dice
                roll=$(shuf -i 1-6 -n 1)
                case $dice in
                        [1-6])  if [ "$dice" -eq "$roll" ] ; 
                                then message="Right! How do you do that, $player?\n$cheater"; cash=$((cash+20));
                                else message="Wrong! My dice showed $roll, $player!\n$cheater"; cash=$((cash-10)); 
                                fi ;;
                        quit) break 2 ;;
                        add) message="$player, you are cheater!"; cheater='By the way, you are cheating.'; cash=$((cash+1500)) ;;
                        rem) message="Excuse me, what???"; cheater=''; cash=$((cash-1000)) ;;
                        *) message="Try again, $player\n" ;;
                esac    
        fi
done

