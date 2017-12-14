# S3C2 Laurel Kuang

def Factorial(x):
    if x==1:
        return 1
    else:
        return Factorial(x-1)*x

def BunnyEars(n):
    if n==0:
        return 0
    else:
        return 2+BunnyEars(n-1)

def Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

def BunnyEars2(n):
    if n==0:
        return 0
    elif n%2 == 1:
        return 2+BunnyEars2(n-1)
    else:
        return 3+BunnyEars2(n-1)

def Triangle(n):
    if n==0:
        return 0
    else:
        return n+Triangle(n-1)

def SumDigits(n):
    if n//10==0:
        return n
    else:
        return n%10 + SumDigits(n//10)

def Count7(n):
    if n//10==0:
        if n==7:
            return 1
        else:
            return 0
    elif n%10==7:
        return 1+Count7(n//10)
    else:
        return Count7(n//10)

def Count8(n):
    if n<8:
        return 0
    elif n%10==8:
        return 1+Count8(n//10)
    elif n%10==8 and (n%100)//10==8:
        return 2+Count8(n//10)
    else:
        return Count8(n//10)

def PowerN(base,n):
    if n==1:
        return base
    return base*PowerN(base,n-1)

def CountX(str):
    if len(str)==0:
        return 0
    elif str[0]=="x":
        return 1+CountX(str[1:])
    else:
        return CountX(str[1:])

def CountHi(str):
    if len(str)<2:
        return 0
    elif str[0:2]=="hi":
        return 1+CountHi(str[2:])
    else:
        return CountHi(str[1:])

def ChangeXY(str):
    if len(str)==0:
        return ""
    elif str[0]=="x":
        return "y"+ChangeXY(str[1:])
    else:
        return str[0]+ChangeXY(str[1:])

def ChangePi(str):
    if len(str)<2:
        return str
    elif str[0:2]=="pi":
        return "3.14"+ChangePi(str[2:])
    else:
        return str[0]+ChangePi(str[1:])

def NoX(str):
    if len(str)==0:
        return ""
    elif str[0]=="x":
        return NoX(str[1:])
    else:
        return str[0]+NoX(str[1:])

def Array6(nums,n):
    if len(nums)==0:
        return False
    elif nums[n]==6:
        return True
    else:
        return Array6(nums,n+1)

def Array11(nums,n):
    if len(nums)==0:
        return 0
    elif nums[n]==11:
        return 1+Array11(nums,n+1)
    else:
        return Array11(nums,n+1)

def Array220(nums,n):
    if len(nums)<2:
        return False
    elif (nums[n+1])/(nums[n])==10:
        return True
    else:
        return Array220(nums,n+2)

def AllStar(str):
    if len(str)<=1:
        return str
    else:
        return str[0]+"*"+AllStar(str[1:])

def PairStar(str):
    if len(str)<=1:
        return str
    elif str[0]==str[1]:
        return str[0]+"*"+str[1]+PairStar(str[2:])
    else:
        return str[0]+PairStar(str[1:])

def EndX(str):
    if len(str)<=1:
        return str
    elif str[0]=="x":
        return EndX(str[1:])+"x"
    else:
        return str[0]+EndX(str[1:])

def CountPairs(str):
    if len(str)<2:
        return 0
    elif str[0]==str[2]:
        return 1+CountPairs(str[1:])
    else:
        return CountPairs(str[1:])

def CountAbc(str):
    if len(str)<3:
        return 0
    elif str[0:3]=="abc" or str[0:3]=="aba":
        return 1+CountAbc(str[1:])
    else:
        return CountAbc(str[1:])

def Count11(str):
    if len(str)<=1:
        return 0
    elif str[0:2]=="11":
        return 1+Count11(str[2:])
    else:
        return Count11(str[1:])

def StringClean(str):
    if len(str)<=1:
        return str
    elif str[0]==str[1]:
        return StringClean(str[1:])
    else:
        return str[0]+StringClean(str[1:])

def CountHi2(str):
    if len(str)<=1:
        return 0
    elif str[0:3]=="xhi":
        return CountHi2(str[3:])
    elif str[0:2]=="hi":
        return 1+CountHi2(str[2:])
    else:
        return CountHi2(str[1:])

def ParenBit(str):
    if str[0]!="(":
        return ParenBit(str[1:])
    if str[-1]!=")":
        return ParenBit(str[:-1])
    return str

def NestParen(str):
    if len(str)<=2:
        if str=="" or str=="()":
            return True
        else:
            return False
    elif str[0]=="(" and str(-1)==")":
        return NestParen(str[1:-1])
    else:
        return False

def StrCount(str,sub):
    if len(sub)>len(str):
        return 0
    elif str[0:len(sub)]==sub:
        return 1+StrCount(str[len(sub):],sub)
    else:
        return StrCount(str[1:],sub)

def StrCopies(str,sub,n):
    if len(sub)>len(str):
        if n==0:
            return True
        else:
            return False
    elif str[0:len(sub)]==sub:
        return StrCopies(str[len(sub):],sub,n-1)
    else:
        return StrCopies(str[1:],sub,n)

def StrDist(str,sub):
    if str[0:len(sub)]!=sub:
        return StrDist(str[1:],sub)
    elif str[-len(sub):]!=sub:
        return StrDist(str[0:-1],sub)
    else:
        return len(str)
