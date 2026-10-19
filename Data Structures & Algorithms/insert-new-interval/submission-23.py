class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
        Output: [[1,6]]

        [-1:0]       [3:4]
                    [4:6]
              [1:3]
            - - - - - - - - - - - 
            0 1 2 3 4 5 6 7 8 9 

              [   1:6   ]
            - - - - - - - - - - - 
            0 1 2 3 4 5 6 7 8 9 
        
        Initiate res = [], 
        for i in range(len(intervals)):
            if end of the new <= the start of old
                res.append the new
                return res + intervals[i:]
            elif start of new >= end of old
                res.append the current old
            else:
                new = [(min(old start, new start), max(old end, new end))
        res.append(new)
        return res
        """
        res=[]

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),
                               max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res