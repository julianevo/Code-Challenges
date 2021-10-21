Each query is represented as a pair of indices (i, j). For each query, perform the following operations:

Select the ith-smallest value among the black cells. In case of a tie, select the one with the lower row number. If there is still a tie, select the one with the lower column number;
Select the jth-smallest white cell using the same process;
Find the average value of these two cells;
If the average value is a whole integer, replace both of the selected cells with the found average value;
Otherwise, replace the cell of the greater value with the average rounded up to the nearest integer, and replace the cell of the smaller value with the average rounded down to the nearest integer.
Your task is to return the resulting matrix after processing all the queries.

matrix = [[2, 0, 4],
          [2, 8, 5],
          [6, 0, 9],
          [2, 7, 10],
          [4, 3, 4]]
and queries = [[0, 0], [1, 3]], the output should be

meanAndChessboard(matrix, queries) = [[1, 2, 4],
                                      [2, 8, 5],
                                      [6, 0, 9],
                                      [2, 7, 10],
                                      [4, 3, 3]]

The average of the 0th black cell and the 0th white cell is (0 + 2) / 2 = 1, so both cells are replaced with 1.
The average of the 1st black cell and the 3rd white cell is (1 + 4) / 2 = 2.5, so the 1 is replaced with floor(2.5) = 2 and the 4 is replaced with ceil(2.5) = 3.


matrix = [[1, 9, 10, 8],
          [3, 4, 4, 4]]
and queries = [[2, 3], [3, 2]], the output should be

meanAndChessboard(matrix, queries) = [[1, 9, 9, 7],
                                      [3, 4, 4, 6]]

The average of the 2nd black cell and the 3rd white cell is (8 + 10) / 2 = 9, so both cells are replaced with 9.
The average of the 3rd black cell and the 2nd white cell is (9 + 4) / 2 = 6.5, so the 9 is replaced with ceil(6.5) = 7 and the 4 is replaced with floor(6.5) = 6.

def meanAndChessboard (matrix,queries):
