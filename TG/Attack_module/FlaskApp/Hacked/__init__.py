"""Haked Flask interface"""
from flask import Flask,request,send_file,send_from_directory
from subprocess import Popen,PIPE
import os


CMDs=None
player=None
ip = None
flask = Flask("Hacked")

if os.path.exists('./extremeinsecure'):
    print('./extremeinsecure')
    flask.root_path=os.path.join(flask.root_path+"/extremeinsecure/")

@flask.route("/")
def home():
        return send_file("index.htm")

@flask.errorhandler(404)
def notfound():
    return '''
           <b>Dette er ikke siden du leter etter!</b><br>
           <p>Kraften vil lede deg {}</p>
           '''

@flask.route("/<folder>/<name>")
def sendFromfolder(folder,name):
    return send_from_directory(folder, name)

@flask.route("/<folder>/<folder1>/<name>")
def sendFromfolder2(folder,folder1,name):
    print(name)
    return send_from_directory(folder+"/"+folder1, name)

@flask.route("/<name>", methods=['GET', 'POST'])
def Post(name):
           if request.method != 'POST':
                   b = send_file("{}".format(name))
                   return b
           else:
                a=request.form["filename"]
                b=CMDs.getCommand(a)
                return "<div>"+a+"<br/>"+b.name+" "+str(b.points)+"</div>"