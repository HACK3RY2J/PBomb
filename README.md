PBomb
An open-source SMS/call bomber for Linux And Termux.


Note:
The script requires working network connection to work.

No balance will be deducted for using this script to send SMS/calls.

While doing infinite bombing use 2-3 seconds delay and 10 to 20 threads for maximum performance.

Don't put spaces in between phone number (Ex- 99999 99999)

Make sure you are using the latest version of PBomb

Make sure you are using Python v3.

Here's how you can check it. Type this command in your terminal.

$ python -V
If output looks like Python 3 - Congrats, Python 3 is installed properly.

Do not use this to harm others.
This script is only for educational purposes or to prank.
None of the developers/contributors are responsible for the misuse of PBomb.

Features:
Lots of integrated SMS/call APIs
Unlimited and super-fast bombing
International bombing available
Call bombing
Frequent updates
Automatic updating mechanism
Easy to use and embed in code
Usage:
Run these commands to run PBomb

> For Termux:
Notice:

git installation methods are not universal and do differ between distributions, so, installing git as per instructions below may not work. Please check out how to install git for your Linux distribution. Commands below provide instructions for Debian-based systems.

To use the bomber type the following commands in Termux:

pkg install git
pkg install python
git clone https://github.com/HACK3RY2J/PBomb.git
cd PBomb
chmod +x PBomb.sh
./PBomb.sh
> For Linux:
Notice:

git installation methods are not universal and do differ between distributions, so, installing git as per instructions below may not work. Please check out how to install git for your Linux distribution. Commands below provide instructions for Debian-based systems.

To use the bomber type the following commands in Linux terminal:

sudo apt install git
git clone https://github.com/HACK3RY2J/PBomb.git
cd PBomb
chmod +x PBomb.sh
sudo bash PBomb.sh
> For macOS:
To use the bomber type the following commands in macOS terminal:

# Install Brew: 

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install dependencys:

brew install git
brew install python3
sudo easy_install pip
sudo pip install --upgrade pip
git clone https://github.com/HACK3RY2J/PBomb
cd PBomb
chmod +x PBomb.sh

# Run PBomb:

sudo bash PBomb.sh
