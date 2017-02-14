#!/usr/bin/env python3

from random import randint
from io import *
from os import system
"""
Generates A interface file with random IP's for each interface
caN MAKE ANY NUMBER OF RANDOM NTERFACERS specified from the _config file

"""
s=list()
_n=10

class Conductor:
    """the builder of the class"""
    def __init__(self,Constructor,n):
        self._constructor=Constructor
        self.n=n

    def ConstructIface(self):
        """Builds the interface"""
        self._constructor.getConfig()
        self._constructor.Construct()
        self._constructor.nameSet(self.n)
        self._constructor.addressSet(self.n,s)
        self._constructor.gatewaySet(self.n)

    def get_Interface(self):
        """REturns said interface"""
        return self._constructor.interface

class Constructor:
    def __init__(self):
        """The Abstract Constructor"""
        self.interface=None
        self.config=None
        self.ip = None


    def Construct(self):
        """
        Creates New Interface Class and Sets Global Configs
        """
        self.interface = Interface()
        self.interface.inet = "static"
        self.interface.netmask=self.config.split()[5]

    def getConfig(self,config="../_config"):
        """Gets info from _cofnig File"""
        with open(config,'r') as config:
            self.config = config.read()
            try:
                self.ip=self.config.split()[3].split('.')
            except:
                pass

class ManagementConstructor(Constructor):
    """Constructs the Management Interface usually Eth0
    Address can be specifyed in _config
    """
    def nameSet(self,n):
        self.interface.name="eth0"
    def addressSet(self,n,s):
        self.interface.address=self.config.split()[1]
    def gatewaySet(self,n):
        self.interface.gateway = self.interface.address[0:11]+"5"

class RegularConstructor(Constructor):
    """
    Constructs the "Dummy" interfaces that the user is going to scan and atack
    these are generated with random ip's
    """
    def nameSet(self,n):
        self.interface.name = "eth0:{}".format(n)
    def addressSet(self,n,s):
        while True:
            a=randint(0,254)
            if a not in s:
                self.interface.address = "10.0.0.{}".format(a)
                s.append(a)
                return a

    def gatewaySet(self,n):
        self.interface.gateway = "10.0.0.1"

class loopbackConstructor(Constructor):
    """
    Creates the loopback interface lo
    """

    def nameSet(self,n):
        self.interface.str ='''
auto lo
iface lo inet loopback
             '''

    def addressSet(self,n,s):
        pass

    def gatewaySet(self,n):
        pass

class Interface:
    def __init__(self):
        """the bace interface class """
        self.name = None
        self.inet = None
        self.address = None
        self.netmask = None
        self.gateway = None
        self.str="""
auto {}
iface {} inet {}
address {}
netmask {}
gateway {}
        """

    def __str__(self):
        try:
            return  self.str.format(self.name,self.name,self.inet,self.address,self.netmask,self.gateway)
        except:
            return self.str

class InterfaceFile:
    def __init__(self):
        """The Class wich generates the intergface file"""

        self.name = "interfaces"
        self.path = "/etc/network/{}".format(self.name)
        self.text = open(self.path,"r").read()

        """Lo interface"""
        self.locon = Conductor(loopbackConstructor(),0)
        self.locon.ConstructIface()
        self.lo=self.locon.get_Interface()

        """Eth0 or MAnagement"""
        self.eth0con = Conductor(ManagementConstructor(),0)
        self.eth0con.ConstructIface()
        self.eth0 = self.eth0con.get_Interface()


        """the regular interrfaces"""
        self.PseudoInterfacescon = list()
        self.PseudoInterfaces = list()
        [self.PseudoInterfacescon.append(Conductor(RegularConstructor(),i))for i in range(0,_n)]
        [i.ConstructIface() for i in self.PseudoInterfacescon]
        [self.PseudoInterfaces.append(i.get_Interface())for i in self.PseudoInterfacescon]

    def WriteAllIfaces(self):
        """Takes all the interfaces and writes them to the file"""
        system("echo " " > {}".format(self.path))
        self.WriteToFile(self.lo)
        self.WriteToFile(self.eth0)
        for i in self.PseudoInterfaces:
            self.WriteToFile(i)

    def WriteToFile(self,iface):
        """writes a interface to the interface file"""
        with open(self.path,"a") as file:
            file.write(iface.__str__())


def main():
    """For testing"""

    ifacefile = InterfaceFile()
    ifacefile.WriteAllIfaces()
if __name__=="__main__":main()
