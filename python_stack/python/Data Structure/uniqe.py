class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        HashMap = {}
        for i in s:
            if i in HashMap:
                HashMap[i] += 1
            else: 
                HashMap[i] = 1

        for i in range(len(s)):
            if HashMap[s[i]] == 1:
                return i
        return -1 

