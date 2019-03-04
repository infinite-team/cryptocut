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

path = os.path.dirname(os.path.abspath(__file__))

TheFilePath = os.path.join(path, "Files", "words-list.txt")

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

print(RandomGenerator(2))
