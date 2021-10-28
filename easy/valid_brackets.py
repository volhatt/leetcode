"""
https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Example 1:
Input: s = "()[]{}"
Output: true

Example 2:
Input: s = "(]"
Output: false

Example 3:
Input: s = "([)]"
Output: false

Example 4:
Input: s = "{[]}"
Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'
"""

def valid_brackets(s):
    """
    time O(n) - n - length of s
    space O(n)
    :param st: string with brackets, str
    :return: if string is valid, boolean
    """
    pair = dict(('()', '[]', '{}'))
    st = []
    for x in s:
        print(f"start loop circle {st}")
        if x in '([{':
            print(f"x {x}")
            st.append(x)
            print(st)
        elif len(st) == 0 or x !=pair[st.pop()]:

            return False
    return len(st) == 0

# the same logic just a little bit simplier to understand
def valid_brackets1(s: str) -> bool:
    char_dict = {"(": ")", "{": "}", "[": "]"}
    new_list = []
    count = 0
    for char in s:
        if char in char_dict :
            new_list.append(char)
        elif len(new_list) > 0 and char == char_dict[new_list[-1]]:
            new_list.pop()
        else:
            count += 1
    if len(new_list) + count > 0:
        return False
    else:
        return True

# longer runtime , only if other chars are not in string
def isValid(s: str) -> bool:
    for i in range(int(len(s)/2)):
        s = s.replace('[]', '').replace('()', '').replace('{}', '')
        if len(s) == 0:
            return True
    if len(s) != 0:
        return False

# a little naive but the same idea
def isValid1(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for x in s:
        if x in mapping:
            if stack and stack[-1] == mapping[x]:
                stack.pop()
            else:
                # this covers the case that the string starts with a closing bracket
                return False
        else:
            stack.append(x)
    if stack:
        return False
    else:
        return True

print(valid_brackets('([)]([)]')) # False
print(valid_brackets('{[()]()}'))  # True

print(valid_brackets1('([)]([)]'))  # False
print(valid_brackets1('{[()]()}'))  # True

print(isValid('{[dd()]()}'))
print(isValid1('{[()]()}'))
