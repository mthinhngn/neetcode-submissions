class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Input: intervals = [[1,3],[1,5],[6,7]]
        Output: [[1,5],[6,7]]


                       [6:7]
              [ 1 : 5 ]
              [1:3]
            - - - - - - - - - - - 
            0 1 2 3 4 5 6 7 8 9 
        
        It doesnt sorted yet, so we have to sort it: O(nlogn)    Space: O(n) 
        
        Pseudo:
        Sort the intervals
        Initiate the res[] add the first interval

        Iterate the start, end in interval from [1:]
            #[-1][1]
            lastE = the end of the latest interval in res
            if start less or equal the latest in res
                update our last interval in res = max(lastE, end of current interval)
            else:
                res.append([start and end of current interval])
        return res

        """

        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1],end)
            else:
                res.append([start,end])
        return res 

