# S3C2 Laurel Kuang
# Recursion 2

def GroupSum(Start,nums,Target):
    if Target==0:
        return True
    elif Start>len(nums)-1 and Target!=0:
        return False
    else:
        return GroupSum(Start+1,nums,Target) or GroupSum(Start+1,nums,Target-nums[Start])
    
def GroupSum6(Start, nums, Target):
    if Target==0:
        return True
    elif Start=len(nums) and Target!=0:
        return False
    elif nums[Start]==6:
        return GroupSum6(Start+1,nums,Target-nums[Start])
    else:
        GroupSum6(Start+1,nums,Target) or GroupSum6(Start+1,nums,Target-nums[Start])

def GroupNoAdj(Start,nums,Target):
    if Target==0:
        return True
    elif Start>=len(nums) and Target!=0:
        return False
    else:
        GroupNoAdj(Start+1,nums,Target) or GroupNoAdj(Start+2,nums,Target-nums[Start])

def GroupSum5(Start,nums,Target):
    if Target==0:
        return True
    elif Start==len(nums) and Target!=0:
        return False
    elif nums[Start]%5==0:
        return GroupSum5(Start+1,nums,Target-nums[Start])
    elif nums[Start]%5==0 and nums[Start+1]==1:
        return GroupSum5(Start+2, nums, Target-nums[Start])
    else:
        return GroupSum5(Start+1,nums,Target) or GroupSum5(Start+1,nums,Target-nums[Start])

def GroupSumClump(Start,nums,Target):
    if Target==0:
        return True
    elif Start>=len(nums) and Target!=0:
        return False
    elif Start<len(nums)-1:
        if nums[Start]==nums[Start+1]:
            return GroupSumClump(Start+2,nums,Target) or GroupSumClump(Start+2,nums,Target-2*(nums[Start]))
    else:
        return GroupSumClump(Start+1,nums,Target) or GroupSumClump(Start+1,nums,Target-nums[Start])

def SplitArray(nums,x=0,y=0,Start=0):
    if Start==len(nums) and x==y:
        return True
    elif Start>=len(nums) and x!=y:
        return False
    else:
        return SplitArray(nums,x+nums[Start],y,Start+1) or SplitArray(nums,x,y+nums[Start],Start+1)

def SplitOdd10(nums,x=0,y=0,Start=0):
    if Start>=len(nums):
        if x%2==1 and y%10==0:
            return True
        elif x%10==0 and y%2==1:
            return True
        else:
            return False
    else:
        return SplitOdd10(nums,x+nums[Start],y,Start+1) or SplitOdd10(nums,x,y+nums[Start],Start+1)            
            
def Split53(nums,x=0,y=0,Start=0):
    if Start==len(nums) and x==y:
        return True
    elif Start==len(nums) and x!=y:
        return False
    elif nums[Start]%3==0:
        return Split53(nums,x,y+nums[Start],Start+1)
    elif nums[Start]%5==0:
        return Split53(nums,x+nums[Start],y,Start+1)
    else:
        return Split53(nums,x,y+nums[Start],Start+1) or Split53(nums,x+nums[Start],y,Start+1)
