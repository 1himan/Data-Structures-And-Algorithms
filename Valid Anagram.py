# this is my solution and its fucking wrong
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArray=[]
        for character in s:
            sArray.append(character)
        tArray=[]
        for character in t:
            tArray.append(character)
        length=len(sArray)
        if length!=len(tArray):
            return False
        for si in range(length):
            for ti in range(length):
                if sArray[si]==tArray[ti]:
                    tArray.pop(ti)
                    sArray.pop(si)
                    break
        if sArray!=tArray:
            return False
