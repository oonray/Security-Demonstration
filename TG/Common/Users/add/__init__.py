#!/usr/bin/env python3

from os import system

packages =["dchroot","debootstrap"]

[system("sudo apt-get install {}".format(pack)) for pack in packages]
system("groupadd ssh-users")



class LinuxUser:
    def __init__(self,name,passwd):
        self.name =name
        self.passwd= passwd

    def setPaSS(self):
        print("[*] Changing Password for: {}".format(self.name))
        system('echo "{}:{}" | chpasswd '.format(self.name,self.passwd))

    def changePasswd(self ,passwd):
        self.passwd = passwd
        self.setPaSS()

    def add(self):
        print("[*] adding {}".format(self.name))
        if system("useradd -G ssh-users {} -p {}".format(self.name,self.passwd)):
           self.setPaSS()


with open("_config") as config:
    config = config.read()
    configuration = config.split()
    root = LinuxUser(name="root",passwd=config[7])
    user = configuration[11].split(',')
    password = configuration[13].split(',')

generatedUsers= [LinuxUser(name=user[i],passwd=password[i]) for i in range(0,len(user))]
[i.add() for i in generatedUsers]
root.changePasswd(configuration[7])


depPath=[
    "/lib/linux-vdso.so.1",
    "/usr/lib/arm-linux-gnueabihf/libarmmem.so",
    "/lib/arm-linux-gnueabihf/libselinux.so.1",
    "/lib/arm-linux-gnueabihf/libacl.so.1",
    "/lib/arm-linux-gnueabihf/libacl.so.1",
    "/lib/arm-linux-gnueabihf/libc.so.6",
    "/lib/ld-linux-armhf.so.3",
    "/lib/ld-linux-armhf.so.3",
    "/lib/arm-linux-gnueabihf/libdl.so.2",
    "/lib/arm-linux-gnueabihf/libattr.so.1",
    "/lib/arm-linux-gnueabihf/libpthread.so.0",
    "/lib/linux-vdso.so.1",
    "/usr/lib/arm-linux-gnueabihf/libarmmem.so",
    "/lib/arm-linux-gnueabihf/libncurses.so.5",
    "/lib/arm-linux-gnueabihf/libtinfo.so.5",
    "/lib/arm-linux-gnueabihf/libdl.so.2",
    "/lib/arm-linux-gnueabihf/libc.so.6",
    "/lib/ld-linux-armhf.so.3",
    "/lib/linux-vdso.so.1",
    "/usr/lib/arm-linux-gnueabihf/libarmmem.so",
    "/lib/arm-linux-gnueabihf/libc.so.6",
    "/lib/ld-linux-armhf.so.3",
    "/lib/arm-linux-gnueabihf/libpcre.so.3"
]

system("mkdir /Jail/")
system("mkdir /Jail/Joe")
system("mkdir /Jail/Joe/dev")
system("mkdir /Jail/Joe/etc")
system("mkdir /Jail/Joe/lib")
system("mkdir /Jail/Joe/usr")
system("mkdir /Jail/Joe/home/")
system("mkdir /Jail/Joe/home/joe")
system("cp ./wordlist /Jail/Joe/home/joe")
system("echo {} > /Jail/Joe/home/joe/howToWin.txt".format("You must unshadow root password from the passwd file. This password must be sendt to the webserver."))
system("mkdir /Jail/Joe/bin")
system("mkdir /Jail/Joe/usr/bin")
system("mknod -m 666 /Jail/Joe/dev/null c 1 3")
system("sudo cp /etc/ld.so.cache /Jail/Joe/etc")
system("sudo cp /etc/ld.so.conf /Jail/Joe/etc")
system("sudo cp /etc/nsswitch.conf /Jail/Joe/etc")
system("sudo cp ./passwd /Jail/Joe/etc")
system("sudo cp ./shadow /Jail/Joe/etc")
system("sudo cp cp /etc/hosts /Jail/Joe/etc")
system("sudo cp /bin/ls /Jail/Joe/bin")
system("sudo cp /bin/cat /Jail/Joe/bin")
system("sudo cp /bin/bash /Jail/Joe/bin")
[system("sudo cp {} /Jail/Joe/lib/".format(i))for i in depPath]

root.changePasswd(configuration[9])
[generatedUsers[i].changePasswd(password[i]) for i in range(0,len(generatedUsers))]
system("sudo cat ./sshd_config > /etc/ssh/sshd_config")

system("/etc/init.d/ssh restart")



