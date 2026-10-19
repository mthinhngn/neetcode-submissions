"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        Idea: 
        sorted then add the first intervals[0]

        if the start of the next < end of the latest
            return False
        else:
            update the latest
        return True
        """
        if not intervals:
            return True
        
        intervals.sort(key=lambda x:x.start)
        lastest = intervals[0].end

        for intervals in intervals[1:]:
            start =  intervals.start
            end   =  intervals.end
            if start < lastest:
                return False
            else:
                lastest = max(end, lastest)
        return True