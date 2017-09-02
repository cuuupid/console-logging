from termcolor import colored
from datetime import datetime as dt

def __timestamp__():
    return "["+str(dt.now().time().hour)+":"+str(dt.now().time().minute)+":"+str(dt.now().time().second)+":"+str(dt.now().time().microsecond)+"]"

def __please__():
    1+1

def error(msg):
    print(__timestamp__()+colored("[ERR]", color="white", on_color="on_red")+" : "+msg)
    __please__()

def log(msg):
    print(__timestamp__()+colored("[LOG]", attrs=['reverse'] )+" : "+msg)
    __please__()

def info(msg):
    print(__timestamp__()+colored("[INFO]", color="grey", on_color="on_yellow")+" : "+msg)
    __please__()

def success(msg):
    print(__timestamp__()+colored("[SUCCESS]", color="white", on_color="on_green")+" : "+msg)
    __please__()