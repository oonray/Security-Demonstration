"""
The idea is to let the user defends agains a AI bot who try to steal info

HE will get a shell with commands and a shell with a packet scan

Scappy will be used to listen to packets
Http packets will be printet in full detail


Rpi01 Atacket
hosts the ai

Rpi2 Defender
is a firewall with listeners on different ports with routes the traffic

Rpi3 contains the info

num of ports=10
no arp requests due to packet flood and so on
"""
