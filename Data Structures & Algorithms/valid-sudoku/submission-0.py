class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #sets for rows columns and the 9 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)]for _ in range(3)]

        # getting values at each position on board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                #checking for dupes
                if val in rows[r] or val in cols[c] or val in boxes[r//3][c//3]:
                    return False
                #when its not a dupe add it
                rows[r].add(val)
                cols[c].add(val)
                boxes[r//3][c//3].add(val)
                
        return True

            



        