"""
Formerly known as Project Exploit
Now Known as Attak module


############################################################################
To Do...
############################################################################
Update previous project form last year...
remove the gui and just let it run with text...
get and post can be handled port widse instead of with flask mabye?
############################################################################
"""
import os
import Attack_module.FlaskApp.Hacked as HFlask
import Attack_module.FlaskApp.Normal as NFlask
import Attack_module.Commands as CMDs
import Attack_module.Player as Player
import Attack_module.Timer as Timer
import Attack_module.Database.Player as DB
import Common.Config as Config

CMDs.config=Config.get('OldRootPasswd')
DB.connect(DB.db)
HFlask.player,NFlask.player = Player,Player
HFlask.CMDs,NFlask.CMDs = CMDs,CMDs
#NFlask.flask.run()
HFlask.flask.run()