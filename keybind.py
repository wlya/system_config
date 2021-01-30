import gi
import os, sys
import signal

gi.require_version('Gtk', '3.0')
gi.require_version('Keybinder', '3.0')

from gi.repository import Gtk
from gi.repository import Keybinder

signal.signal(signal.SIGCHLD, signal.SIG_IGN)


def vexit(ff):
    sys.exit()

    
key_array = {
    "<Control><Alt>q": vexit,
    '<Control><Alt>a': "flameshot gui"
}



def callback(keystr, user_data):
    print("Handling", keystr, user_data)
    os.system(key_array[keystr])
    

if __name__ == '__main__':
    keystr = "<Control><Alt>u"
    Keybinder.init()
    for key in key_array:
        res = False
        if type(key_array[key]) == type(''):
            res = Keybinder.bind(key, callback, "Keystring %s (user data)" % key)
        else:
            res = Keybinder.bind(key, key_array[key])
        if not res:
            print('绑定快捷键失败', key, res)
            exit(1)
    Gtk.main()
