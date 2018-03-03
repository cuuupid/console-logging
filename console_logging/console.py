from datetime import datetime as dt
import platform
from termcolor import colored

# Old features
TAGS = {
    'error': colored("[  ERR  ]", color="white", on_color="on_red"),
    'log': colored("[  LOG  ]", attrs=['reverse']),
    'info': colored("[ INFO  ]", color="grey", on_color="on_yellow"),
    'success': colored("[SUCCESS]", color="white", on_color="on_green")
}

if platform.system() == 'Windows':
    TAGS = {
            'error': "[  ERR  ]",
            'log': "[  LOG  ]",
            'info': "[ INFO  ]",
            'success': "[SUCCESS]"
    }

def __timestamp__():
    return "[%d:%d:%d:%d]" % (dt.now().time().hour, dt.now().time().minute, dt.now().time().second, dt.now().time().microsecond)


def __print__(tag="", msg=""):
    print("%s%s : %s" % (__timestamp__(), tag, msg))


def error(msg):
    __print__(tag=TAGS['error'], msg=msg)


def log(msg):
    __print__(tag=TAGS['log'], msg=msg)


def info(msg):
    __print__(tag=TAGS['info'], msg=msg)


def success(msg):
    __print__(tag=TAGS['success'], msg=msg)


# New features
class Console:

    TAGS = {
        'error': colored("[  ERR  ]", color="white", on_color="on_red"),
        'log': colored("[  LOG  ]", attrs=['reverse']),
        'info': colored("[ INFO  ]", color="grey", on_color="on_yellow"),
        'success': colored("[SUCCESS]", color="white", on_color="on_green")
    }

    VERBOSITY = 4

    SHOW_TIME = True

    def __init__(self):
        if platform.system() == 'Windows':
            self.monotone()

    def __timestamp__(self):
        if self.SHOW_TIME:
            return "[%d:%d:%d:%d]" % (dt.now().time().hour, dt.now().time().minute, dt.now().time().second, dt.now().time().microsecond)
        else:
            return ""

    @classmethod
    def __please__(self):
        1 + 1
        return

    def __print__(self, tag="", msg=""):
        print("%s%s : %s" % (self.__timestamp__(), tag, msg))

    def mute(self):
        self.VERBOSITY = 0

    def monotone(self):
        self.TAGS = {
            'error': "[  ERR  ]",
            'log': "[  LOG  ]",
            'info': "[ INFO  ]",
            'success': "[SUCCESS]"
        }
    
    def timeless(self):
        self.SHOW_TIME = False

    def setVerbosity(self, level):
        if level > 5:
            level = 5
        elif level < 0:
            level = 0
        self.VERBOSITY = level

    def __should_i_shutup__(self, l):
        return l > self.VERBOSITY

    def error(self, msg):
        if self.__should_i_shutup__(1):
            return
        self.__print__(tag=self.TAGS['error'], msg=msg)
        self.__please__()

    def log(self, msg):
        if self.__should_i_shutup__(3):
            return
        self.__print__(tag=self.TAGS['log'], msg=msg)
        self.__please__()

    def info(self, msg):
        if self.__should_i_shutup__(4):
            return
        self.__print__(tag=self.TAGS['info'], msg=msg)
        self.__please__()

    def success(self, msg):
        if self.__should_i_shutup__(2):
            return
        self.__print__(tag=self.TAGS['success'], msg=msg)
        self.__please__()

    def secure(self, tag, msg):
        if self.__should_i_shutup__(5):
            return
        self.__print__(tag=colored(tag, color="white",
                                   on_color="on_blue"), msg=msg)
        self.__please__()
