#!/usr/bin/python3
"""
this module returns all the integers representing a pascal's triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        triangle = []
        for row in range(n):
            curr_row = []
            for column in range(row + 1):
                if column == 0 or column == row:
                    curr_row.append(1)
                else:
                    prev_row = triangle[row - 1]
                    curr_row.append(prev_row[column - 1] + prev_row[column])
            triangle.append(curr_row)

        return triangle
