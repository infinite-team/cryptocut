#------------------------------------------------------------------------------
# Copyright (c) 2019, Infinite Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------

import warnings
import inspect
import random
import linecache
import os
import appdirs
import hashlib
from cryptography.fernet import Fernet

path = os.path.dirname(os.path.abspath(__file__))

TheFilePath = os.path.join(path, "Files", "words-list.txt")

appname="CryptoCut"
appauthor="Infinite"

CachePath = appdirs.user_cache_dir(appname,appauthor)
ConfigPath = appdirs.user_config_dir(appname,appauthor)
DataPath = appdirs.user_data_dir(appname,appauthor)
LogPath = appdirs.user_log_dir(appname,appauthor)
StatePath = appdirs.user_state_dir(appname,appauthor)

def FileLen(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def GetVarName(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return str([k for k, v in callers_local_vars if v is var][0])

def TypeChecker(CheckDict):
    '''
    var:type
    var,nowtype,shouldtype
    '''
    Degree=0
    ProblemsList=[]
    AllVars=CheckDict.keys()
    for x in AllVars:
        CompabitableBool=str(type(x)).split("'")[1]==CheckDict.get(x)
        if (CompabitableBool==False):
            ProblemsList.append([GetVarName(x),str(type(x)).split("'")[1],CheckDict.get(x)])
    return ProblemsList

def RandomGenerator(level):
    try:
        RandomObject=random.SystemRandom()
    except:
        RandomObject=random
    Password=""
    if (level==1):
        for i in range (1,2):
            Password+=linecache.getline(TheFilePath,RandomObject.randint(1,FileLen(TheFilePath)))[0:-1]+"-"
        Password+=linecache.getline(TheFilePath,RandomObject.randint(1,FileLen(TheFilePath)))[0:-1]
    if (level==2):
        for i in range (1,5):
            Password+=linecache.getline(TheFilePath,RandomObject.randint(1,FileLen(TheFilePath)))[0:-1]+"-"
        Password+=linecache.getline(TheFilePath,RandomObject.randint(1,FileLen(TheFilePath)))[0:-1]
    if (level==3):
        for i in range (1,10):
            Password+=linecache.getline(TheFilePath,RandomObject.randint(1,FileLen(TheFilePath)))[0:-1]+"-"
        Password+=linecache.getline(TheFilePath,RandomObject.randint(1,FileLen(TheFilePath)))[0:-1]
    return Password

def HashGenerator(Level):

    RandomString = RandomGenerator(Level)
    hash = hashlib.sha224(b"%s" %(RandomString.encode('utf8'))).hexdigest()
    with open('keyhash.txt', 'a') as the_file:
        the_file.write(hash)
    return(hash)

def EncryptMethodOne(PlainText):
    
    KeyFile = open('key.txt','r')
    key = KeyFile.read()
    KeyFile.close()
    key = key[2:]
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(b"%s" %(PlainText.encode('utf8')))
    # print(cipher_text)
    return(cipher_text)

def DecryptMethodOne(CipherText):

    KeyFile = open('key.txt','r')
    key = KeyFile.read()
    KeyFile.close()
    key = key[2:]
    cipher_suite = Fernet(key)

    # print(CipherText.encode('utf8'))

    plain_text = cipher_suite.decrypt(b"%s" % (CipherText.encode('utf8')))
    return(plain_text)


# print(RandomGenerator(3))
# HashGenerator(2)
# print(EncryptMethodOne("hello okad"))
# print(DecryptMethodOne(
#     'gAAAAABcoxRm3EXRTxX9jmoSb1EjkpH3gKuHms9MEKWUyzgnxNLmu1gkUzS5JnRfkV6PMRbnGNpk2_iltIWHXji3YDs7kTZtJw=='))

# gAAAAABchfdowRJkNWefsR0ch-v4nBM-ZFNE2enZcxBJQUZjgHBEPEQly8IW5CH8Ln7cX1TFg08fmysBdDee04IOVEJ6-acB_JVBL2vQQegsNCQTL9HZXl4 =
# gAAAAABcoto3P-kWsi5KvseJujXaA-atzDhOrZtxTc_Dkz4d6CkSAl3Zw5Uma28LHNdjk4BCDbQm6-14GpM1NpXGQLMlWh_Xpg =
# gAAAAABcotYmDGDlvyt7WSeEPP5YGtqrz1k3c5WKqBtj3Q5zNPWIUGNRhUzCxOKwRouCgwxH-bSZXqaSkgc-5hiHkqtlllkvJw =
# gAAAAABcotrprNmZIrqeOiWZjj_NeUtkrc_WZgjnWlm3HmtOtzNsrb7wjEZ-oeRlY2I1b9Jn0Nj2FXFatPj0ckf3yIaGq4Oq-A =
# gAAAAABcotsgJlxkiU6u5aT5hR8lLkgBli85HPtPJ7C0Y5CTM9ZOr1Y_fr8b7KpDDXikMruZJaQ4RNSxeWabhPy6gup_bOmJvQ==

# gAAAAABcotw-wjGynf9hYuCsNK37ntXxpES1Lcv7c4EsfeN7NSFzxZVHqbEmWLfpIrj8KbesSAFZKqFX4kJ5q-HH1SZ3D5BCNw = gAAAAABcotw-wjGynf9hYuCsNK37ntXxpES1Lcv7c4EsfeN7NSFzxZVHqbEmWLfpIrj8KbesSAFZKqFX4kJ5q-HH1SZ3D5BCNw =
