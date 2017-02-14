import pickle
import sys

_Rpi01_IP=""
_Rpi02_IP=""
_Rpi03_IP=""

def ge_ips():
    return _Rpi01_IP,_Rpi02_IP,_Rpi03_IP
def dump():
    pickle.dump(_Rpi01_IP,_Rpi02_IP,_Rpi03_IP,open("info.pcl","w"))
def load():
    _Rpi01_IP, _Rpi02_IP, _Rpi03_IP = pickle.load(open("info.pcl","r"))


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: {} <ip01> <ip02> <ip03>")
    else:
        prog,_Rpi01_IP,_Rpi02_IP,_Rpi03_IP = sys.argv

    dump()