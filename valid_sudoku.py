from collections import Counter, defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        final_result = {
            # "row_values": {},
            "box_values": defaultdict(list),
            "column_value": defaultdict(list),
        }
        temp_box = 0

        for index, row in enumerate(board):
            # For validating row values
            # final_result["row_values"][index] = row
            row_values_count = Counter(row)
            row_values_count.pop('.')
            if max(row_values_count.values()) > 1:
                return False
            # For creating a box
            if index in [3,6]:
                temp_box = index
            final_result["box_values"][temp_box].extend(row[:3])
            final_result["box_values"][temp_box+1].extend(row[3:6])
            final_result["box_values"][temp_box+2].extend(row[6:])
            # For fetching values in columns
            for col_index in range(len(row)):
                final_result["column_value"][col_index].append(row[col_index])

        # To Validate all boxes.
        for box in final_result["box_values"]:
            box_values_count = Counter(final_result["box_values"][box])
            box_values_count.pop('.')
            if max(box_values_count.values()) > 1:
                return False

        # To Validate all the columns.
        for column in final_result["column_value"]:
            column_values_count = Counter(final_result["column_value"][column])
            column_values_count.pop('.')
            if max(column_values_count.values()) > 1:
                return False

        return True


a = Solution()
print(a.isValidSudoku(
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    )
)
