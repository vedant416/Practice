class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        data = sorted(intervals, key=lambda x: x[0])

        i = 0
        while i<= len(data):
            s1 = data[i][0]
            e1 = data[i][1]

            if i+1>=len(data):
                break
            
            s2 = data[i+1][0]
            e2 = data[i+1][1]

            if e1 >= s2: 
                new = new = [ s1, max(e1, e2)]
                data[i] = None
                data[i+1] = new
            
            i+=1
        res = []
        for i in data:
            if i:
                res.append(i)
        return res
    