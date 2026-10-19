"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        Input: intervals = [(0,40),(5,10),(15,20)]
        Output: 2 , 
        room1: (0:40)
        room2: (5:10)(15,20)

                                
                  [   5:10   ]  [ 15:20 ]           room2
        [                0:40                 ]     room1
        - - - - - - - - - - - - - - - - - - - -
        0 1 2 3 4 5 6 7 8 9 10   15    20     40

        Using 2 pointer at 2 sorted array start, array end
        start = [0 , 5,15]
        end   = [10,20,40]
        We will compare the start[i] end[i]). 
        If the start[i] < end[i], that mean the meeting is used -> count += 1, 
        we will return the max count we have

        Pseudo:
        #seperate to sorted start, sorted end
        Intiate sorted start array
        Initate sorted end array
        res, count = 0, 0
        Initiate the s,e pointer at each array, both start at beginning

        #Because start always end first
        Iterate while s pointer until it touch the end intervals:
            if start[s] < end[e]:
                move the s
                increase the count
            else:
                decrease the count
                move e
            update res = max(res, count)
        return res
        """

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count =0,0
        s,e = 0,0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                count -= 1
                e += 1
            res = max(res,count)
        return res