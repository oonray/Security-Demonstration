#!/usr/bin/python3

#Imports---------------------------------------------------
import sys,os

path = sys.path
"""sets the sys path so that we may ionclude ../modules"""
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from ProjectExploitDB import *
from ProjectExploitUser import user
from ProjectExploitCreateInterfaces import *
from ProjectExploitConnector import GetSocket
from ProjectExploitFlaskApps import getFlask
from ProjectEcploitGUI import *
from subprocess import *
from threading import _start_new_thread
from ProjectExploitTimer import timer
from time import sleep

"""resets sys path so that we dont list the modules when exploiting the app"""
sys.path = path

"""Randomizes interfaces except Management"""
ifacefile = InterfaceFile()
ifacefile.WriteAllIfaces()
#system("python3 ../ProjectExploitCreateInterfaces.py")
system("/etc/init.d/networking restart")
system("systemctl daemon-reload")
system("/etc/init.d/apache2 stop")

_Time=30
_Type="minutes"

"""The database"""
db = database()

"""The timer"""
timerS = timer(_Time,_Type)

"""Our Lovely players"""
player01 = user(db)

"""The Gui"""
gui = GUI(player01,timerS,db)

"""Sockets used for the User log in, we should be able to close these sockets later"""
a = GetSocket("Listen")


"""Factory returns app as needed"""
hacked = getFlask("hacked",player01,gui)
regular = getFlask("regular",player01,gui)

def timeS():
    print("[Time check]")
    while True:
        #if timerS.startStop == True:
        #    sleep(1)
        #    print(timerS.getTimestr())
        #    print(timerS.times)
        if timerS.timeended():
            print("[TIME ENDED]")
            gui.TimeStop()
            break



def main():
    """ Starts The Hacked interface """
    _start_new_thread(hacked.flask.run,(ifacefile.PseudoInterfaces[0].address,80))
    print("[HackedApp] "+ifacefile.PseudoInterfaces[0].address,80)
    #_start_new_thread(a.bindLocalIface(ifacefile.eth0.address,6688),())
    #
    # a.Accept()

    """Starts all the others"""
    for i in ifacefile.PseudoInterfaces:
            if i.name != ifacefile.PseudoInterfaces[0].name:
                _start_new_thread(regular.flask.run,(i.address,80))
                #_start_new_thread(psuedoSockets.append(GetSocket("Listen",player01,gui).bindLocalIface(i.address,6688)))
            else:
                continue

    """Starts all the other interfaces"""
    gui.PackPage(gui.StartPage)
    gui.StartPage.focus_set()
    gui.StartInputs[0].focus_set()
    _start_new_thread(timeS,())
    gui.mainloop()



if __name__ == "__main__": main()
