# ------------------------------------------------------------------------------
# Copyright (c) 2021, Infinite Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ------------------------------------------------------------------------------

from threading import Thread
import platform
from tools import get_user_key,read_symmetric_key
# detect OS
# install tools for specific OS/distro
# copy files
if (platform.system() == "Darwin"):
    pass
if (platform.system() == "Windows"):
    pass
if (platform.system() == "Linux"):
    pass


def first_run_tui():
    '''
    first setups and creating key's and personal passwords
    '''
    from cryptography.fernet import Fernet
    print("hello from Infinite Team.")
    user_pass = input("enter your password : ").encode()
    user_key = (get_user_key(user_pass))
    # generate a random secret for user using crypto lib
    fernet = Fernet(user_key)
    random_key = Fernet.generate_key()
    symmetric_key = fernet.encrypt(random_key)
    # write the random secret as symmetric_key in symmetric.key
    # TODO : we can use a diffrent path for this
    with open("symmetric.key", "wb") as key_file:
        key_file.write(symmetric_key)
if __name__ == '__main':
    first_run_tui()


# def encrypt(PlainText):
#     KeyFile = open('key.txt','r')
#     key = KeyFile.read()
#     KeyFile.close()
#     key = key[2:]
#     cipher_suite = Fernet(key)
#     cipher_text = cipher_suite.encrypt(b"%s" %(PlainText.encode('utf8')))
#     return(cipher_text)

# def decrypt(CipherText):
#     KeyFile = open('key.txt','r')
#     key = KeyFile.read()
#     KeyFile.close()
#     key = key[2:]
#     cipher_suite = Fernet(key)    
#     plain_text = cipher_suite.decrypt(b"%s" % (CipherText.encode('utf8')))
#     return(plain_text)

# def RandomDict(level):
#     Password=""
#     if (level==1):
#         for i in range (1,2):
#             Password+=linecache.getline(TheFilePath,RandomGenerator(1,FileLen(TheFilePath)))[0:-1]+"-"
#         Password+=linecache.getline(TheFilePath,RandomGenerator(1,FileLen(TheFilePath)))[0:-1]
#     if (level==2):
#         for i in range (1,5):
#             Password+=linecache.getline(TheFilePath,RandomGenerator(1,FileLen(TheFilePath)))[0:-1]+"-"
#         Password+=linecache.getline(TheFilePath,RandomGenerator(1,FileLen(TheFilePath)))[0:-1]
#     if (level==3):
#         for i in range (1,10):
#             Password+=linecache.getline(TheFilePath,RandomGenerator(1,FileLen(TheFilePath)))[0:-1]+"-"
#         Password+=linecache.getline(TheFilePath,RandomGenerator(1,FileLen(TheFilePath)))[0:-1]
#     return Password
# def FileLen(fname):
#     with open(fname) as f:
#         for i, l in enumerate(f):
#             pass
#     return i + 1
# def GetVarName(var):
#     callers_local_vars = inspect.currentframe().f_back.f_locals.items()
#     return str([k for k, v in callers_local_vars if v is var][0])

# def TypeChecker(CheckDict):
#     '''
#     var:type
#     var,nowtype,shouldtype
#     '''
#     Degree=0
#     ProblemsList=[]
#     AllVars=CheckDict.keys()
#     for x in AllVars:
#         CompabitableBool=str(type(x)).split("'")[1]==CheckDict.get(x)
#         if (CompabitableBool==False):
#             ProblemsList.append([GetVarName(x),str(type(x)).split("'")[1],CheckDict.get(x)])
#     return ProblemsList
# def RandomGenerator(x,y):
#     try:
#         RandomObject=random.SystemRandom()
#     except:
#         RandomObject=random
#     return RandomObject.randint(x,y)

# def HashGenerator(Level):
#     RandomString = RandomGenerator(Level)
#     hash = hashlib.sha224(b"%s" %(RandomString.encode('utf8'))).hexdigest()
#     with open('keyhash.txt', 'a') as the_file:
#         the_file.write(hash)
#     return(hash)
# import warnings
# import inspect
# import random
# import linecache
# import hashlib
# import base64

# def DictToFernetCode(InputDictStr=""):
#     HashedPass=hashlib.sha256(InputDictStr.encode("utf-8"))
#     return (base64.urlsafe_b64encode(bytes.fromhex(HashedPass.hexdigest())))

# if __name__ == '__main__':
#     user_key = create_user_key("13811394")
#     fernet = Fernet(user_key)
#     random_key = Fernet.generate_key()
#     symmetric_key = fernet.encrypt(random_key)
#     with open("symmetric.key", "wb") as key_file:
#         key_file.write(symmetric_key)
#     print(symmetric__encrypt("hello",read_symmetric_key()))
#     print(symmetric__decrypt("gAAAAABgWR9JPH2ozm-XmTbyEvEgamS4Fu7jYUKS4p41chCGUcmpmlKHhexu4NqkcLV4cgsOuUrlVoUlOy_mAMO8BH2SkvAIoA==",read_symmetric_key()))
