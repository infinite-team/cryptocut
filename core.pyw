#------------------------------------------------------------------------------
# Copyright (c) 2019, Infinite Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
#------------------------------------------------------------------------------

import notify2
from pynput import keyboard
import configparser

notify2.init("CryptoCut")
DoneNofification = notify2.Notification("Done","Encrypted successfully","notification-message-info")
# DoneNofification.show()


COMBINATIONS = [
    {keyboard.Key.shift, keyboard.Key.ctrl,keyboard.KeyCode(char='A')}
]

# The currently active modifiers
current = set()

def execute():
    print ("Do Something")
    
	config = configparser.ConfigParser()
	config['DEFAULT'] = {'ServerAliveInterval': '45','Compression': 'yes','CompressionLevel': '9'}
	config['bitbucket.org'] = {}
	config['bitbucket.org']['User'] = 'hg'
	config['topsecret.server.com'] = {}
	topsecret = config['topsecret.server.com']
	topsecret['Port'] = '50022'     # mutates the parser
	topsecret['ForwardX11'] = 'no'  # same here
	config['DEFAULT']['ForwardX11'] = 'yes'
	with open('example.ini', 'w') as configfile:
    	config.write(configfile)

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()