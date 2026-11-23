class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_string = []
        t_string = []
        for i in s:
            s_string.append(i)
        
        for j in t:
            t_string.append(j)
        
        sorted_s = sorted(s_string)
        sorted_t = sorted(t_string)
        if sorted_s == sorted_t:
            return True
        return False