"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's
 triangle. ( binomial expansion )
 Example:
Input: rowIndex = 3
Output: [1,3,3,1]
"""


def getRow(rowIndex):
    """
    binomial expansion nyr format eg C(n,r)

    """
    row = [1]
    for x in range(1, rowIndex+1):
        row.append(row[x-1] * (rowIndex - x + 1) // x)
    return row


def getRow1(rowIndex):
    """
    time complexity O(n**2) - n different rows
    and the same space complexity
    """
    result = [[1]]  # fist row always [1]
    print(result[-1])

    for i in range(rowIndex):  # -1 because first row already done above
        # build row - take previous row [-1] and add '0' before and after - temp
        temp = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) + 1):  # building next row - previous row + 1
            row.append(temp[j] + temp[j + 1])
        result.append(row)
    print(result)
    return result[rowIndex]

def getRow2(rowIndex):
    r = [1]
    for _ in range(rowIndex):
        r = [1, *(map(sum, zip(r, r[1:]))), 1]
    return r


print(getRow(3))
print(f"getRow1 {getRow1(3)}")
print(getRow2(3))
