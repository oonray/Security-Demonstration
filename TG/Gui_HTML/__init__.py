import socket
import sys


"""Set up the ports and """
socket_count = range(0,13)
local_IP= ""
remote_IP= ""
gui_IP=""
ports = [22,23,80,8080,21,20,24,25,26,2222]
sockets=[]
[sockets.append(socket.socket(socket.AF_INET,socket.SOCK_STREAM))for i in socket_count]
[sockets[x].bind((local_IP, ports[x])) for x in range(0, len(ports))]
[sockets[x].bind((remote_IP, ports[x])) for x in range(0, len(ports))]
