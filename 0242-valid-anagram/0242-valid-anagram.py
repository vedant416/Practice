class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}
        for x, y in zip(s, t):
            map1[x] = map1.get(x, 0) + 1
            map2[y] = map2.get(y, 0) + 1 
        return map1 == map2
            
        