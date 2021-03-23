#------------------------------------------------------------------------------
# Copyright (c) 2021, Infinite Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------


import os
import appdirs
from cryptography.fernet import Fernet

appname="CryptoCut"
appauthor="Infinite"

path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, "Files", "words-list.txt")
cache_path = appdirs.user_cache_dir(appname,appauthor)
config_path = appdirs.user_config_dir(appname,appauthor)
data_path = appdirs.user_data_dir(appname,appauthor)
log_path = appdirs.user_log_dir(appname,appauthor)
dtate_path = appdirs.user_state_dir(appname,appauthor)


def create_user_key(user_pass):

    '''creating a key baseed on user key'''
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    import base64
    from cryptography.hazmat.backends import default_backend

    user_pass = user_pass.encode()
    # TODO : check if its the first time or user wants to change the pass

    # create a key based on user password
    # TODO : we can use os.urandom(16) or somthing that user want
    salt = b'cryptocut_'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend())
    user_key = base64.urlsafe_b64encode(kdf.derive(user_pass))

    return user_key

def read_symmetric_key(file_name = 'symmetric.key'):
    '''open the key file and check if the user pass is correct'''

    with open(file_name,'rb') as f:
        encrypted_key = f.read()
    user_pass = input("enter your password : ")
    userbase_key = create_user_key(user_pass)
    fernet = Fernet(userbase_key)
    try:
        decrypted_key = fernet.decrypt(encrypted_key)
    except:
        return 0
    return decrypted_key

def symmetric__encrypt(message,key):
    if(not key):
        return "Wrong password !"
    message = message.encode()
    f = Fernet(key)
    return(f.encrypt(message))

def symmetric__decrypt(encrypted_message,key):
    if(not key):
        return "Wrong password !"
    encrypted_message = encrypted_message.encode('utf-8')
    f = Fernet(key)
    return(f.decrypt(encrypted_message).decode('utf-8'))


if __name__ == '__main__':
    print(symmetric__encrypt("hello",read_symmetric_key()))
    print(symmetric__decrypt("gAAAAABgWlN_jy_6a_oacOzJumSPOh6RFOkN1Rha7qjinWieVKS75b_bgXkowI8lpBCH8sDzWYayuOldU9k3ismB-0NcMHF3Ew==",read_symmetric_key()))
