import unittest
from builtins import range, len, print


def snail(matrix):
    if not matrix:
        return []
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

class TestSnail(unittest.TestCase):
    def test_snail(self):
        array = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(snail(array), expected)

        array = [[1,2,3],
                 [8,9,4],
                 [7,6,5]]
        expected = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(snail(array), expected)


if __name__ == '__main__':
    unittest.main()


print(snail([[1,2,3],[4,5,6],[7,8,9]]))