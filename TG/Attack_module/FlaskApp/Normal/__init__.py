"""Haked Flask interface"""
from flask import Flask,request,send_file,send_from_directory
from subprocess import Popen,PIPE
import os


CMDs=None
player=None
gui=None
cmd = None
ip = None

flask = Flask("Normal",static_url_path='')

if os.path.exists('./extremeinsecure'):
    print('./extremeinsecure')
    flask.root_path=os.path.join(flask.root_path+"/extremeinsecure/")


@flask.route("/")
def home():

    #if player.gameStarted != True:
     #   return "Your must register and Start The Gsme"
    #else:
        return send_file("index.htm")


@flask.route("/<name>")
def homesHtml(name):
  #  if player.gameStarted != True:
    #    return "Your must register and Start The Game"
    #else:
        b = send_file("{}".format(name))
        return b

@flask.errorhandler(404)
def notfound():
    return '''
           <b>Dette er ikke siden du leter etter!</b><br>
           <p>Kraften vil lede deg {}</p>
           '''
@flask.route("/<folder>/<name>")
def sendFromfolder(folder,name):
    print(name)
    return send_from_directory(folder, name)

@flask.route("/<folder>/<folder1>/<name>")
def sendFromfolder2(folder,folder1,name):
    print(name)
    return send_from_directory(folder+"/"+folder1, name)