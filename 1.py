class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        for i in xrange(len(nums)):
            k = nums[i]
            if hm.has_key(k):
                hm[k].append(i)
            else:
                hm[k] = [i]
        for k, v in hm.items():
            k2 = target - k
            if k == k2:
                if len(v) > 1:
                    return [v[0], v[1]]
            else:
                if hm.has_key(k2):
                    return [v[0], hm[k2][0]]
