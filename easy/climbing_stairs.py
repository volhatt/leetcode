"""
It takes n steps to reach the top of the stairs. Each time you can either climb
1 or 2 steps. In how many distinct ways can you climb to the top?
1<=n<=45
"""
from math import factorial


def climbing_stairs1(n: int) -> int:
    # create empty array to keep solutions
    dp = [0 for x in range(n+1)]
    # if steps 0 or 1, it is only one way
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

def climbing_stairs2(n):
    output = 0
    for i in range(n // 2 + 1):
        output += factorial(n - i) // (factorial(n - 2 * i) * factorial(i))
    return output

def climbing_stairs3(n):
    a = b = 1
    for i in range(n - 1):
        c = a + b
        a, b = b, c
    return b

def climbing_stairs4(n):
    """
    recursion with memoization
     time O(n),
     Space O(n)
    store keep calculated values to avoid recalculation (the concept of memoization)
    """
    store = {}  # store our calculation
    def helper(n):
        # those are aur base cases, just returns N
        if n == 1 or n == 2:
            return n
        elif n in store:  # memoization (store values to avoid recalculation)
            return store[n]
        else:
            store[n] = helper(n-1) + helper(n-2)
            return store[n]
    return helper(n)

# the same logic as #3
def climbing_stairs5(n):
    """
    buttom up approach ( линейное )
     time complexity O(n)
     Space complexity O(1)
    """
    pre = curr = 1
    temp = 0
    for i in range(1, n):
        temp = curr
        curr += pre
        pre = temp
    return curr


print(climbing_stairs5(5))
print(climbing_stairs4(6))
