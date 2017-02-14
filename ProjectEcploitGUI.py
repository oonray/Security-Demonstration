import tkinter as tk
from tkinter import ttk
from tkinter import StringVar,IntVar
from os import system
from threading import _start_new_thread

"""
the Gui for the app
this is the pølace that wil display info and player stats
"""

class GUI(tk.Tk):
    """GUI class for the hakking app, based on tkinter"""
    def __init__(self,player,timer,db):
        tk.Tk.__init__(self)
        self.pageFrame=ttk.Frame(self)
        self.db =db
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        #self.overrideredirect(1)
        self.geometry("{}x{}+0+0".format(w,h))
        self.pageFrame.pack()
        self.pageFrame.place(relx=.5, rely=.5, anchor="c")
        self.option_add("*Font", "TkDefaultFont 15")
        self.option_add("*Font", "TkTextFont 15")
        self.option_add("*Font", "TkFixedFont 15")

        """Vars used to change values of the labels"""
        self.IntVar = IntVar()
        self.IntVarTime = StringVar()
        self.PointsCommands=[StringVar(),StringVar(),StringVar()]
        self.PlayerName=StringVar()

        """the pointers to the player and the timer class instance"""
        self.player= player
        self.timer = timer

        """the frames named after their functionallity"""
        self.StartPage = ttk.Frame(self.pageFrame)
        self.PointsPage = ttk.Frame(self.pageFrame)
        self.ScoreBoard = ttk.Frame(self.pageFrame)


       # self.imagelogo = ttk.Label(self,image=Image.open("logo.png"))

        """"buttons and frames set up as lists"""
        """Start"""
        self.StartButtons = list()
        self.StartInputs = list()
        self.StartLabel = list()
        """Points"""
        self.PointsButtons=list()
        self.PointsFrames = list()
        self.PointsLabels = list()
        self.PointsLabels3 = list()
        """Score"""
        self.ScoreFrames = list()
        self.ScoreLabelsName = list()
        self.ScoreLabelsTime = list()
        self.ScoreLabelsPoints = list()

        """Page Generators Call"""
        #self.Image.pack(side="LEFT")
        self.GenStartPage()
        self.GenPointsPage()
        self.GenScoreBoard()

    def TimeStop(self):
        print(self.timer.getTimestr())
        print("Time is up!")
        self.addLastCommand("Time is up!")
        try:
                        self.player.updateTimeint(1000000000000000)
                        self.player.updateTimestr("DNF")
        except:
                        pass
    def stop(self):
        self.player.setGameStopped()
        self.timer.stop()
        self.timer.getTimestr()
        print("[GAME STOPPED] You scored: {}".format(self.player.points))
        quit()

    def PackPage(self,page):
        """used to pack the frames"""
        page.pack(fill="both",expand=True)

    def addPoints(self,points):
        """sets the points label based on the players current points"""
        self.IntVar.set(points)

    def addLastCommand(self, message):
        """adds the last commans to the gui
            see Points Page generator for more info
        """
        g=0
        for i in (0,1,2):
            if self.PointsCommands[i].get()==" ":
                self.PointsCommands[i].set(message)
                break
            else:
                g+=1
        if g>=3:
            self.PointsCommands[0].set(self.PointsCommands[1].get())
            self.PointsCommands[1].set(self.PointsCommands[2].get())
            self.PointsCommands[2].set(message)
        else:
            pass

    def forget(self,t):
        """Hides a frame"""
        t.pack_forget()

    def GenScoreBoard(self):
        """Generates the high Score page, this is contrived from the 5 uppermost players """
        self.ScoreFrames.append(ttk.Frame(self.ScoreBoard))
        users = self.db.GetTopPlayers()


        """Adds Name"""
        self.ScoreLabelsName.append(ttk.Label(self.ScoreFrames[0],text="Name"))
        for i in users:
            self.ScoreLabelsName.append(ttk.Label(self.ScoreFrames[0],text=i[0]))

        """Adds time"""
        self.ScoreLabelsTime.append(ttk.Label(self.ScoreFrames[0],text="Time"))
        for i in users:
            self.ScoreLabelsTime.append(ttk.Label(self.ScoreFrames[0],text=i[1]))

        """Adds Points"""
        self.ScoreLabelsPoints.append(ttk.Label(self.ScoreFrames[0],text="Points"))
        for i in users:
            self.ScoreLabelsPoints.append(ttk.Label(self.ScoreFrames[0],text=i[2]))

        for i in self.ScoreFrames:
            i.pack()

        """Gridding of the labels"""
        for i in range(0,len(self.ScoreLabelsName)):
            self.ScoreLabelsName[i].grid(column=1,row=i,padx=10)
        for i in range(0,len(self.ScoreLabelsPoints)):
            self.ScoreLabelsPoints[i].grid(column=2,row=i,padx=10)

        for i in range(0,len(self.ScoreLabelsTime)):
            self.ScoreLabelsTime[i].grid(column=3,row=i,padx=10)

        """BNolding of the main labels"""
        self.ScoreLabelsName[0].config(font="-weight bold")
        self.ScoreLabelsPoints[0].config(font="-weight bold")
        self.ScoreLabelsTime[0].config(font="-weight bold")

    def GenPointsPage(self):
        """generates all the items in the frame thet displays ponts naem and comamnds"""
        self.forget(self.StartPage)
        self.IntVar.set(self.player.points)
        for i in self.PointsCommands:
            i.set(" ")

        """Frames to Group each infividual 'LAbel' """
        self.PointsPageFrame=ttk.Frame(self.PointsPage)
        self.PointsFrames.append(ttk.Frame(self.PointsPageFrame))
        self.PointsFrames.append(ttk.Frame(self.PointsPageFrame))
        self.PointsFrames.append(ttk.Frame(self.PointsPageFrame))
        self.PointsFrames.append(ttk.Frame(self.PointsPageFrame))


        """The actuall frames"""
        self.PointsLabels.append(ttk.Label(self.PointsFrames[0],text="Name"))
        self.PointsLabels.append(ttk.Label(self.PointsFrames[0],textvariable=self.PlayerName))

        self.PointsLabels.append(ttk.Label(self.PointsFrames[1],text="Commands"))
        self.PointsLabels.append(ttk.Label(self.PointsFrames[1],textvariable=self.PointsCommands[0]))
        self.PointsLabels.append(ttk.Label(self.PointsFrames[1],textvariable=self.PointsCommands[1]))
        self.PointsLabels.append(ttk.Label(self.PointsFrames[1],textvariable=self.PointsCommands[2]))

        self.PointsLabels.append(ttk.Label(self.PointsFrames[2],text="Points"))
        self.PointsLabels.append(ttk.Label(self.PointsFrames[2],textvariable=self.IntVar))

        self.PointsLabels.append(ttk.Label(self.PointsFrames[3],text="Time"))
        self.PointsLabels.append(ttk.Label(self.PointsFrames[3],textvariable=self.IntVarTime))

        self.PointsButtons.append(ttk.Button(self.PointsPageFrame,text="Restart Computer",command=lambda : system("sudo restart")))
        self.PointsButtons.append(ttk.Button(self.PointsPageFrame,text="Stop Game",command=lambda : self.stop()))

        """the gridding of the frames"""
        self.PointsPageFrame.pack()
        g=0
        for i in self.PointsFrames:
            i.grid(row=0,column=g,padx=10,pady=5,sticky="N")
            g+=1
        del g

        for i in (0,2,6):
            self.PointsLabels[i].grid(row=0,column=0)
            self.PointsLabels[i].config(font="-weight bold")
            if i ==0:
                self.PointsLabels[1].grid(row=1,column=0)
            if i == 2:
                self.PointsLabels[3].grid(row=1,column=0)
                self.PointsLabels[4].grid(row=2,column=0)
                self.PointsLabels[5].grid(row=3,column=0)
            if i == 6:
                self.PointsLabels[7].grid(row=1,column=0)
            if i == 8:
                self.PointsLabels[9].grid(row=1,column=0)

        for i in (0,1):
            self.PointsButtons[i].grid(column=i,row=1,padx=5,pady=10)

    def GenStartPage(self):
        """generates the page that displays the registratinon page with a start button"""
        self.forget(self.PointsPage)
        self.StartPageFrame=ttk.Frame(self.StartPage)
        self.StartButtons.append(ttk.Button(self.StartPageFrame,text="Start",command=lambda:self.Start()))
        self.StartLabel.append(ttk.Label(self.StartPageFrame,text="Name"))
        self.StartLabel.append(ttk.Label(self.StartPageFrame,text="Email"))
        self.StartLabel.append(ttk.Label(self.StartPageFrame,text="Phone"))
        self.StartInputs.append(ttk.Entry(self.StartPageFrame))
        self.StartInputs.append(ttk.Entry(self.StartPageFrame))
        self.StartInputs.append(ttk.Entry(self.StartPageFrame))
        self.StartInputs[2].insert(0,"+47")

        self.StartPageFrame.pack()
        for i in range(0,len(self.StartInputs)):
            try:
                    self.StartLabel[i].grid(row=(i+1),column=(1),)
            except:
                pass
            try:
                    self.StartInputs[i].grid(row=(i+1),column=(2))
            except:
                pass
        for i in range(0,len(self.StartButtons)):
            self.StartButtons[i].grid(column=(i+1))

    def Start(self):
        """the functin executed by the start button this actually starts the game, dough the web servers are alreaddy generated"""
        self.timer.th.start()
        self.player.name=self.StartInputs[0].get()
        self.PlayerName.set(self.player.name)
        self.player.email=self.StartInputs[1].get()
        self.player.phone=self.StartInputs[2].get()
        self.forget(self.StartPage)
        self.PackPage(self.ScoreBoard)
        self.PackPage(self.PointsPage)
        self.player.addToDb()
        self.player.setGameStarted()



def main():
    """'For testing putposes"""

    from ProjectExploitTimer import timer
    from ProjectExploitUser import user
    from ProjectExploitDB import database
    import sys

    timer = timer("0:5:0","minutes")
    db=database("Users.db")
    player=user(name="Alex",db=db)
    player.points=5

    gui=GUI(player,timer,db)
    gui.PackPage(gui.StartPage)
    gui.StartPage.focus_set()
    gui.mainloop()
if __name__ == "__main__":main()