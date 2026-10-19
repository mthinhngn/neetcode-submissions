class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        A = [start1, end1]
        B = [start2, end2]
        --------------------------------------------------
        1. START OVERLAP
        A: [1--------5]
        B:     [3--------7]

        Condition:
        start2 < end1
        3 < 5  -> overlap
        --------------------------------------------------
        2. START NOT OVERLAP / TOUCHING
        A: [1----3]
        B:       [3----5]

        Condition:
        start2 == end1
        3 == 3  -> NOT overlap
        --------------------------------------------------
        3. COMPLETELY SEPARATE
        A: [1----3]
        B:          [4----6]

        Condition:
        start2 > end1
        4 > 3  -> NOT overlap
        --------------------------------------------------
        4. WHOLE INTERVAL INSIDE ANOTHER
        A: [1--------------10]
        B:     [3----6]

        B is completely inside A

        Condition:
        start2 >= start1
        end2 <= end1
        -> overlap
        --------------------------------------------------
        5. CURRENT INTERVAL CONTAINS PREVIOUS
        A:     [3----6]
        B: [1--------------10]

        A is completely inside B
        -> overlap
        --------------------------------------------------
        6. END OVERLAP
        A: [1--------5]
        B:       [4--------8]

        B starts before A ends
        4 < 5
        -> overlap
        --------------------------------------------------
        7. SAME START
        A: [1--------5]
        B: [1----3]

        Same start:
        start1 == start2

        -> overlap
        Keep the one ending earlier:
        [1,3]
        --------------------------------------------------
        8. SAME END
        A: [1--------5]
        B:    [3-----5]

        Same end:
        end1 == end2
        -> overlap

        Either ending point is the same.
        --------------------------------------------------
        9. EXACT SAME INTERVAL

        A: [1--------5]
        B: [1--------5]

        -> overlap
        One must be removed.
        --------------------------------------------------
        MAIN RULE:
        if start2 < end1:
            OVERLAP

        if start2 >= end1:
            NOT OVERLAP

        WHEN OVERLAP:
        keep the smaller ending point
        prevEnd = min(prevEnd, end)

        Does the next interval START
        before the previous interval ENDS?

        Input: intervals = [[1,2],[2,4],[1,4]]
        Output: 1, [1,4]
        
                 [1,    4]
                    [2, 4] 
                 [1,2]
                - - -  - - - - - - -
                0 1 2  3 4 5 6 7 8 9
        #intervals.sort() means sort start,end
        #intervals.sort(key=lambda x:x[0]) means only sort start
        Sort the intervals 
        Initiate res = 0
        Initiate lastestE = our first intervals end

        Iterate start, end thru index 1 to end intervals
            #think about what make them not overlap 
            if start of current >=  end of latestE
                update the latest E = new current end
            else:
                res += 1
                #why, because if they overlap, we want the less end for more room 
                update latestE = min(lastedE, current E)
        return res
        """
        intervals.sort()
        res = 0
        prevE = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevE:
                prevE = end
            else:
                res += 1
                prevE = min(prevE, end)
        return res            