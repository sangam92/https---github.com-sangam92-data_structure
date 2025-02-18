class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        
        cols = [set() for _ in range(9)]  # Track numbers in columns
        boxes = [set() for _ in range(9)]  # Track numbers in 3x3 boxes

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":  # Skip empty cells
                    continue
            
                box_index = (r // 3) * 3 + (c // 3)  # Calculate box index

                # Check for duplicates in row, column, and box
                if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                    return False
            
            # Add number to respective sets
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

        return True       