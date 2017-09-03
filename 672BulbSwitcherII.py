class Solution(object):
    def flip(self,situation,operation, n):
        for i in xrange(n):
            if operation & (1<<0):
                situation = self.flipBit(situation,i)
            if operation & (1<<1):
                if i%2==1:
                    situation = self.flipBit(situation,i)
            if operation & (1<<2):
                if i%2==0:
                    situation = self.flipBit(situation,i)
            if operation & (1<<3):
                if i%3==0:
                    situation = self.flipBit(situation,i)
        return situation

    
    def flipBit(self,situation,i):
        bit=(1<<i)
        if situation & bit:
            situation-=bit
        else:
            situation+=bit
        return situation
            
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        1,4,7,10,13
        101,110,111
        """
        operations=set()
        operations.add(0)
        for i in xrange(m):
            newOperations=set()
            for operation in operations:
                for j in xrange(4):
                    newOperations.add(self.flipBit(operation,j))
            operations = newOperations
        initialSituation = (1<<n)-1
        situations = set()
        for operation in operations:
            situations.add(self.flip(initialSituation,operation,n))
        return len(situations)