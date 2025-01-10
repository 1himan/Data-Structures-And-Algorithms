# this is my solution - and its fuckin wrong 
class Solution:
    def getConcatenation(self, nums):
        length=len(nums)
        ans=[]*2*length
        n=0
        for i in range(length*2):
            n+=1
            ans[i+n]=nums[i]
        return ans


# another solutions for this same question:
def getConcatenation(nums):
        return nums+nums

def getConcatenation(nums):
    result=[]
    for _ in range(2):
         result.extend(nums)
    return result