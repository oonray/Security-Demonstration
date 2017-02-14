import os
import time
from threading import *
"""
The timer module
keeps track of how manny seconds the user has been using

"""
class timer:
    def __init__(self,time=30,type="minutes"):
        """the Counters"""
        self.timeEnded=False
        self.type=type
        self.times=time
        self.seconds=0
        self.minutes=0
        self.houers=0
        self.RealMinutes = 0
        """start counter used in the Start function"""
        self.startStop = False
        self.th=Thread(target=self.start)

    def timeended(self):
        return self.timeEnded
    def CheckTime(self):
        if self.startStop == True:
            if self.times == 0:
                    return True

            if self.RealMinutes < self.times:
                    return True
            else:
                    self.timeEnded = True
                    return False
        else:
            return False

    def getTimeint(self):
        return int("{}{}{}".format(self.houers,self.minutes,self.seconds))

    def getTimestr(self):
        return "{}:{}:{}".format(self.houers,self.minutes,self.seconds)

    def start(self):
          """starts the timer"""
          print("[TIME sTART]")
          self.startStop = True
          while self.CheckTime():
              time.sleep(1)
              self.seconds+=1
              if self.seconds >= 60:
                  self.seconds = 0
                  self.minutes += 1
                  self.RealMinutes += 1
                  if self.minutes >=60:
                      self.minutes=0
                      self.houers+=1



    def stop(self):
        """stops the timer"""
        self.startStop = False

def main():
    time=timer("0:0:5","seconds")
    time.th.start()
    n=time.getTimestr()
    while True:
        if n != time.getTimestr():
            print(time.getTimestr())
            n=time.getTimestr()

if __name__=="__main__":main()
