#!/bin/bash
mkdir /Jail/
mkdir /Jail/Joe
/Jail/Joe/dev
mkdir /Jail/Joe/etc
mkdir /Jail/Joe/lib
mkdir /Jail/Joe/usr
mkdir /Jail/Joe/home/
mkdir /Jail/Joe/home/joe
cp ./Passwords/wordlist /Jail/Joe/home/joe
echo "You must unshadow root password from the passwd file. This password must be sendt to the webserver." > /Jail/Joe/home/joe/howToWin.txt
mkdir /Jail/Joe/bin
mkdir /Jail/Joe/usr/bin
mknod -m 666 /Jail/Joe/dev/null c 1 3
sudo cp /etc/ld.so.cache /Jail/Joe/etc
sudo cp /etc/ld.so.conf /Jail/Joe/etc
sudo cp /etc/nsswitch.conf /Jail/Joe/etc
sudo cp ./Passwords/passwd /Jail/Joe/etc
sudo cp ./Passwords/shadow /Jail/Joe/etc
sudo cp cp /etc/hosts /Jail/Joe/etc
sudo cp /bin/ls /Jail/Joe/bin
sudo cp /bin/cat /Jail/Joe/bin
sudo cp /bin/bash /Jail/Joe/bin
#Remember to add libs in the script
