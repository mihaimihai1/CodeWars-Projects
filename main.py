import unittest
from builtins import range, len, print

def snail(map):
    nmap = []
    top, right, bottom, left = 0, len(map) - 1, len(map) - 1, 0

    while (top <= bottom and left <= right):
        for i in range(left, right + 1):
            nmap.append(map[top][i])
        top += 1
        for i in range(top, bottom + 1):
            nmap.append(map[i][right])
        right -= 1
        for i in range(right, left - 1, -1):
            nmap.append(map[bottom][i])
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            nmap.append(map[i][left])
        left += 1
    return nmap


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