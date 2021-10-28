"""
https://leetcode.com/problems/reverse-integer/
Given a signed 32-bit integer x, return x with its digits reversed. If reversing
 x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
  then return 0.
"""
import math


# my solution
def reverse(x):
    """
    runtime 24ms ( better 98 %)
    memory usage 14.3 mb ( less then 45 %)
    """
    if x == 0:
        return 0
    negative = False
    reversed_string = ''

    for i in str(x):
        if i == '-':
            negative = True
            continue
        reversed_string = i + reversed_string
    if negative:
        reversed_string = '-' + reversed_string
    result = int(reversed_string)
    return result if result in range(-2 ** 31, 2 ** 31 - 1) else 0

def reverse1(x: int) -> int:
    """
    runtime O(1) and memory O(lig(x)) almost the same as previous

    """
    result = 0
    is_negative = x < 0
    x = -x if is_negative else x
    while x > 0:
        result = 10 * result + x % 10
        x //= 10
    if result not in range(-2 ** 31, 2 ** 31 - 1):
        return 0
    return -result if is_negative else result

print(reverse(-123))
print(reverse1(-123))
