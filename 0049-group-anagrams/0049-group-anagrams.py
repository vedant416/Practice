class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            hm[key].append(s)
            
        return hm.values()
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # key() : value(list)
#         hm = collections.defaultdict(list)
        
#         for string in strs:
#             countArray = [0] * 26
            
#             # build key
#             for char in string:
#                 index = ord(char) - ord("a")
#                 countArray[index] += 1 
#             key = tuple(countArray)
            
#             # add string using key 
#             hm[key].append(string)
#         return hm.values()