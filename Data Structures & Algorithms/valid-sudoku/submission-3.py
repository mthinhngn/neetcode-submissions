class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
           0   1   2   3   4   5     6   7   8
        0["1","2","."|".","3","."|",".",".","."],
        1["4",".","."|"5",".","."|",".",".","."],
        2[".","9","8"|".",".","."|",".",".","3"],
    
        3["5",".","."|".","6","."|",".",".","4"],
        4[".",".","."|"8",".","3"|",".",".","5"],
        5["7",".","."|".","2","."|",".",".","6"],
    
        6[".",".","."|".",".","."|","2",".","."],
        7[".",".","."|"4","1","9"|",".",".","8"],
        8[".",".","."|".","8","."|",".","7","9"]

        3 hashmap: rows, cols, box = set(),set(), set()
        Run r thru board       #because 9x9 grid
            Run c thru board[0] 
                get n at each location 

                if n == ".":
                    continue
                
                Assign the index position and n for (r,n)
                Assign the index position and n for (c,n)
                Assign the index position and n for (r//3,c//3,n)

                if rkey in row or ckey in col or bkey in box
                    return False
                add n to r set
                add n to c set
                add n to b set
        return False 
        """
        rows, cols, boxs = set(),set(), set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                n = board[r][c]
                
                if n == ".":
                    continue
                
                rk = (r,n)
                ck = (c,n)
                bk = (r//3,c//3,n)
                
                if (rk in rows or
                    ck in cols or
                    bk in boxs):
                    return False
                
                rows.add(rk)
                cols.add(ck)
                boxs.add(bk)
        return True

