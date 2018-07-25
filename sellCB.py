import subprocess
from pyautogui import press, typewrite, hotkey, click
from time import sleep
import config
#import WindowMgr


def wrapper(mit, ohne, before, after, seperator, platinum):
    seperator = cleanSep(seperator)
    if len(mit) == 0:
        sellString =  withoutPrice(ohne)
    elif len(ohne) == 0:
        sellString = withPrice(mit, platinum)
    else:
        sellString = withPrice(mit, platinum)  + seperator + withoutPrice(ohne)

    return 'echo '+ before +" " + sellString + " " + after + ' |clip'


def cleanSep(sep):
    return sep.replace("|", " ")

def withPrice(d, platinum):
    return "".join([(k + " " + str(d[k]) + platinum) for k in d])

def withoutPrice(l):
    return ''.join(l)

def sell(text):
    return subprocess.check_call(text, shell=True)

##def swapWindow():
##    w = WindowMgr.WindowMgr()
##    w.find_window_wildcard("WARFRAME")
##    w.set_foreground()
##    click()
    

def autoPrint(s=0):
    sleep(s)
    press('T')
    sleep(.333)
    hotkey('ctrl','v')
    press('enter')

if __name__ == '__main__':
    sell(wrapper(config.preisMit, config.preisOhne , config.before, config.after, config.seperator, config.platinum))
##    swapWindows()
##    autoPrint(2)


