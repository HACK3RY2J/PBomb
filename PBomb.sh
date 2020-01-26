#!/bin/bash
clear
echo -e "\e[4;31m Panda Hackers Productions !!! \e[0m"
echo -e "\e[1;34m Presents \e[0m"
echo -e "\e[1;32m PBomb \e[0m"
echo "Press Enter To Continue"
read a1
if [[ -s update.pandahackers ]];then
echo "All Requirements Found...."
else
echo 'Installing Requirements....'
echo .
echo .
apt install figlet toilet python curl -y
apt install python3-pip
pip install -r requirements.txt
echo This Script Was Made By Panda Hackers >update.pandahackers
echo Requirements Installed....
echo Press Enter To Continue...
read upd
fi
while :
do
rm *.xxx >/dev/null 2>&1
clear
echo -e "\e[1;31m"
figlet PBomb
echo -e "\e[1;34m Created By \e[1;32m"
toilet -f mono12 -F border Panda Hackers
echo -e "\e[4;34m This Bomber Was Created By Panda Hackers \e[0m"
echo -e "\e[1;34m For Any Queries Mail Me!!!\e[0m"
echo -e "\e[1;32m           Mail: Pandahackers127@gmail.com \e[0m"
echo -e "\e[4;32m   YouTube Page: https://www.youtube.com/c/PandaHackers \e[0m"
echo " "
echo -e "\e[4;31m Please Read Instruction Carefully !!! \e[0m"
echo " "
echo "Press 1 To  Start SMS Bomber "
echo "Press 2 To  Start Call Bomber "
echo "Press 3 To  Update (Works On Linux And Linux Emulators) "
echo "Press 4 To  View Features "
echo "Press 5 To  Exit "
read ch
if [ $ch -eq 1 ];then
clear
echo -e "\e[1;32m"
rm *.xxx >/dev/null 2>&1
python3 bomber.py
rm *.xxx >/dev/null 2>&1
exit 0
elif [ $ch -eq 2 ];then
clear
echo -e "\e[1;32m"
echo 'Call Bomb By Panda Hackers'> call.xxx
python3 bomber.py call
rm *.xxx >/dev/null 2>&1
exit 0
elif [ $ch -eq 3 ];then
clear
apt install git -y
echo -e "\e[1;34m Downloading Latest Files..."
git clone https://github.com/HACK3RY2J/PBomb
if [[ -s PBomb/PBomb.sh ]];then
cd PBomb
cp -r -f * .. > temp
cd ..
rm -rf  PBomb >> temp
rm update.Pandahackers >> temp
rm temp
chmod +x PBomb.sh
fi
echo -e "\e[1;32m PBomb Will Restart Now..."
echo -e "\e[1;32m All The Required Packages Will Be Installed..."
echo -e "\e[1;34m Press Enter To Proceed To Restart..."
read a6
./PBomb.sh
exit
elif [ $ch -eq 4 ];then
clear
echo -e "\e[1;33m"
figlet PBomb
echo -e "\e[1;34mCreated By \e[1;34m"
toilet -f mono12 -F border Panda Hackers 
echo  " "
echo -e "\e[1;32m                   Features\e[1;34m"
echo "  [+] Unlimited And Super-Fast Bombing"
echo "  [+] International Bombing"
echo "  [+] Call Bombing "
echo "  [+] Protection List"
echo "  [+] Automated Future Updates"
echo "  [+] Easy To Use And Embed in Code"
echo -e "\e[1;32m                   Contributors\e[1;33m"
echo -e "\e[1;33m      [*]  Panda Hackers  \e[1;31m"
echo "         [-] Mail At: pandahackers127@gmail.com"
echo ""
echo ""
echo -e "\e[1;31m This Script is Only For Educational Purposes or To Prank.\e[0m"
echo -e "\e[1;31m Do not Use This To Harm Others. \e[0m"
echo -e "\e[1;31m I Am Not Responsible For The Misuse Of The Script. \e[0m"
echo -e "\e[1;32m Make Sure To Update it If It Does not Work.\e[0m"
echo  " "
echo -e "\e[4;31m That's All !!!\e[0m"
echo -e "\e[1;34m For Any Queries Mail Me!!!\e[0m"
echo -e "\e[1;32m           Mail: Pandahackers127@gmail.com \e[0m"
echo -e "\e[1;32m       Whatsapp: https://bit.ly/PH-Group \e[0m"
echo -e "\e[4;32m   YouTube Page: https://www.youtube.com/c/PandaHackers \e[0m"
echo "Press Enter To Go Home"
read a3
clear
elif [ $ch -eq 5 ];then
clear
echo -e "\e[1;31m"
figlet PBomb
echo -e "\e[1;34m Created By \e[1;32m"
toilet -f mono12 -F border Panda Hackers
echo -e "\e[1;34m For Any Queries Mail Me!!!\e[0m"
echo -e "\e[1;32m           Mail: Pandahackers127@gmail.com \e[0m"
echo -e "\e[1;32m       Whatsapp: https://bit.ly/PH-GROUP \e[0m"
echo -e "\e[4;32m   YouTube Page: https://www.youtube.com/c/PandaHackers \e[0m"
echo " "
exit 0
else
echo -e "\e[4;32m Invalid Input !!! \e[0m"
echo "Press Enter To Go Home"
read a3
clear
fi
done
