class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numStr = str(num)
        return int(self.helper(numStr))
    
    def helper(self, numStr):
        if len(numStr)<1:
            return numStr
        maxDigit=int(numStr[0])
        maxPos=0
        for i in xrange(1,len(numStr)):
            currentDigit = int(numStr[i])
            if currentDigit>=maxDigit:
                maxDigit=currentDigit
                maxPos=i
        if maxPos>0 and maxDigit>int(numStr[0]):
            retStr=numStr[maxPos]
            if len(numStr)>1:
                retStr+=numStr[1:maxPos]
                retStr+=numStr[0]
                retStr+=numStr[maxPos+1:]
            return retStr
        else:
            return numStr[0]+self.helper(numStr[1:])