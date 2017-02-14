from distutils.core import setup
import py2exe,os,sys
import argparse

arg = argparse.ArgumentParser(description="Make target windows Binary")
arg.add_argument("-t",dest="target",help="the target .py script to make exe",type=str)
arg.add_argument("-z",dest="zip",help="specify to be delivered as zip",type=str)
args=arg.parse_args()

sys.argv.append('py2exe')
setup(
    options={"py2exe":{'bundle_files':1}},
    windows=[{"script":args.target}],
    zipfile=None if not args.zip else True
)