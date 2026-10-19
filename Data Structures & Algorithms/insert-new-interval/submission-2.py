class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """ 
            [2 : 5]
                [4:6]
          [1:3]
        - - - - - - - - - ----
        0 1 2 3 4 5 6 7 8 9 

        Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
        Output: [[1,6]]

          [ 1 :   6 ]  
        - - - - - - - - - ----
        0 1 2 3 4 5 6 7 8 9 

        Edge case:
        - newI go before the end of the current we has (end newI[1] < start old[i][0])
        - newI go after the end of the current we has ([1:2], new[3:4]) (start new[0] > old[i][1])
        - newI overlapping with the currend we has
            (update the newI when overlap = [min(start of old, start of new),max(end of old, end of new)]
        
        Initiate an empty res[]

        for i running the intervals array
            if the end of new < start of old
                append newI to res
                return res + intervals
            elif the start of new > end of old
                append the old
            else:
                newI = [min(start old, start new), max(end new, end old)]
        
        res.append(newI)
        return res
        """
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0],newInterval[0]), max(intervals[i][1],newInterval[1])]
        res.append(newInterval)
        return res



        
