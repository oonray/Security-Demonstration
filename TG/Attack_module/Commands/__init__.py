"""this class define commasnds as a class
       it is useful when scoring points and denying or allowing certan commands
    """
config=None

class command:
   def __init__(self,name,points):
         self.name = name
         self.points = points

def getCommand(name):
        """Generates leagal commands as a dict with theur points and returns a commad object based on your input"""

        Commands = {
            "ls":command("ls",10),
            "ls -al":command("ls",10),
            "cat users.json":command("cat",50),
            "pwd":command("pwd",10),
            "cat feedbak.htm":command("cat",0),
            "cat feedback_submitted.htm":command("cat",0),
            "cat index.htm":command("cat",10),
            "cat news.htm":command("cat",0),
            "cat process.php":command("cat",30),
            "cat products.htm":command("cat",0),
            "cat search.htm":command("cat",0),
            "cat search_results.htm":command("cat",0),
            "cat services.htm":command("cat",0),
            "cat toc.htm":command("cat",0),
            config:command("gotRoot",50)
        }
        return Commands.get(name,command("Not Allowed",0))


