import math
import warnings

def PrimeBool(x):
	if (x==1):
		return False
	c=math.floor(x**0.5)
	while (c>1):
		if (x%c==0):
			return False
		c-=1
	return True

def xCheckerList(UpTo,BoolFunc=PrimeBool):
	x=1
	list=[]
	while (x<=UpTo):
		if(BoolFunc(x)):
			list.append(x)
		x+=1
	return list

def xNumberOfList(Number,BoolFunc=PrimeBool,StartNum=1):
	counter=StartNum
	list=[]
	while (Number>0):
		if (BoolFunc(counter)):
			list.append(counter)
			Number-=1
		counter+=1
	return list

def IntegerBool(x):
	return x-math.floor(x)==0

def NaturalBool(x):
	return (IntegerBool(x) and x>0)

def WholeBool(x):
	return (IntegerBool(x) and x>=0)



def MersennePrimeBool(x):
	if(PrimeBool(x)):
		return NaturalBool(math.log((x+1),2))
	return False

def PowOfMersennePrimeBool(x):
	return (PrimeBool((2**x)-1))

'''
def GCD():


def
'''

def xNumberDivisorsList(x,From=1,To=None,BoolFuncOnlyDivisors=None):
	"""

	"""
	counter=From
	if (To!=None):
		if(To>x):
			warnings.warn("It's reasonless to try find natural divisor bigger than the given number!")
		max=To
	else:
		max=x
	list=[]
	if(BoolFuncOnlyDivisors==None):
		while(counter<=max):
			if(x%counter==0):
				list.append(counter)
			counter+=1
	else:
		while(counter<=max):
			if(x%counter==0):
				if(BoolFuncOnlyDivisors(counter)):
					list.append(counter)
			counter+=1
	return list

def xNumberPrimeDivisorsDict(x):
	i=0
	PrimeDivisorsList=xNumberDivisorsList(x,1,x,PrimeBool)
	PrimeDivisorsCountList=[0]*len(PrimeDivisorsList)
	while (x!=1):
		if(x%PrimeDivisorsList[i]==0):
			x=x/PrimeDivisorsList[i]
			PrimeDivisorsCountList[i]+=1
			i-=1
		i+=1
	return (dict(zip(PrimeDivisorsList,PrimeDivisorsCountList)))

def xNumberOfFibonacciList(x):
	if (x==1):
		return [1]
	list=[1,1]
	i=0
	while (x>2):
		list.append(list[i]+list[i+1])
		i+=1
		x-=1
	return list

def FibonacciBool(x):
	FibonacciList=xNumberOfFibonacciList(x)
	return (FibonacciList[len(FibonacciList)-1]==x)
'''
number and string checks
fibonachi
equation solver
'''

def GoldbachDoublesList(x):
	"""
	"""
	list=[]
	if (x%2!=0):
		raise ValueError("Goldbach conjecture works on even numbers!")
	listofprimedivisors=xCheckerList(x,PrimeBool)
	sp=0
	ep=len(listofprimedivisors)-1
	while(sp<=ep):
		if(listofprimedivisors[sp]+listofprimedivisors[ep]>x):
			ep-=1
		if(listofprimedivisors[sp]+listofprimedivisors[ep]<x):
			sp+=1
		if(listofprimedivisors[sp]+listofprimedivisors[ep]==x):
			list.append(tuple([listofprimedivisors[sp],listofprimedivisors[ep]]))
			ep-=1
			sp+=1
	return list
