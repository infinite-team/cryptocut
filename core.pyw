#------------------------------------------------------------------------------
# Copyright (c) 2019, Infinite Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
#------------------------------------------------------------------------------
import keyboard
import pyperclip
import pyautogui
import time
from tools import EncryptMethodOne,DecryptMethodOne

def KeyboadStuff():
    try:
        OrgClipboard = pyperclip.paste()
        time.sleep(0.25)
        pyperclip.copy('')
        SelectionDetect = str(pyautogui.hotkey('ctrl', 'c'))
        Selection = pyperclip.paste()
        print("Selection: "+str(len(Selection)))
        if(len(Selection) > 0):
            pyautogui.hotkey('ctrl', 'c')
        else:
            pyautogui.hotkey('ctrl', 'a', 'x')
        # time.sleep(0.5)
        text = pyperclip.paste()
        text = str(text)
        print(text)
        print(text[0:6])
        if(text[0:7] == 'gAAAAAB' and text[-1] == '='):
            print('--------------------------------------------------------------')
            print("En message")
            print('--------------------------------------------------------------')
            print('Encrypt text:', text)
            t = DecryptMethodOne(text)
            # print(type(t))
            t = str(t)
            t = t[2:-1]
            print(pyperclip.copy(t))
            time.sleep(0.25)
            pyautogui.typewrite(t, interval=0.08)
            time.sleep(0.25)
            print(pyperclip.copy(OrgClipboard))
        else:
            print('--------------------------------------------------------------')
            print("not En message")
            print('--------------------------------------------------------------')

            t = EncryptMethodOne(text)
            t = str(t)
            t = t[2:-1]
            
            print(pyperclip.copy(t))
            time.sleep(0.25)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.25)
            print(pyperclip.copy(OrgClipboard))
    except MemoryError:
        print("Error")

def main():
    keyboard.add_hotkey('ctrl+shift+q', KeyboadStuff)
    keyboard.wait()
if __name__ == '__main__':
    main()

# gAAAAABcot7JjMSsHcg4oot7H4idSKcJyYAljmwFOv9vSsIhpo--Hgy4RbcY1kCHvy0HJpDYGIPBfp60UJC42ySHRH6bf3HL-Q ==
# gAAAAABcot7JjMSsHcg4oot7H4idSKcJyYAljmwFOv9vSsIhpo--Hgy4RbcY1kCHvy0HJpDYGIPBfp60UJC42ySHRH6bf3HL-Q ==
