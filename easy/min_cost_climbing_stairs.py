"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
- - - - - - - -
Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
- - - - - - - -
Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
- - - - - - - -
Constraints:
- 2 <= cost.length <= 1000
- 0 <= cost[i] <= 999
- - - - - - - - - -
Explanation:
This is top-down dynamic programming (DP) approach solution. - build-up of a
number of smaller subproblems, starting at the end.
At each step we can consider the answer to be combined cost of the curent step,
plus the lesser result of the total cost of each of the solutions starting at the
next 2 steps ( we can solve the smallest problem first, and the build down from
there).
for the last 2 steps the answer - their individual cost. For the third to last
step - that step's cost + lower of the last 2 steps. ( it could be done with
DP array but in this solution we store values "in place" )
(Note: If we choose to not modify the input, we could create a DP array to store
 this information at the expense of O(N) extra space.)
Time Complexity: O(N) where N is the length of cost
Space Complexity: O(1) or O(N) if we use a separate DP array
"""


# Solution
def min_cost_climbing_stairs1(cost):
    for i in range(len(cost) - 3, -1, -1):  # starts from el 7, end at cost[0] backwards
        cost[i] += min(cost[i + 1], cost[i + 2])
        print(f"{cost[i]}  i {i}, cost[i+1] {cost[i + 1]} cost[i+2] {cost[i + 2]} ")
    return min(cost[0], cost[1])


ar = [10, 15, 20]  # 55
# print(min_cost_climbing_stairs(ar))


# this is very close solution but with adding current_step instead save price in array cost
# this solution takes less time and memory usage ! ( a little bit )
def min_cost_climbing_stairs2(cost):
    step1, step2 = 0, 0
    for i in range(len(cost) - 1, -1, -1):  # starts from last, moving backwards
        current_step = cost[i] + min(step1, step2)
        step1 = step2
        step2 = current_step
        print(f"current_step {current_step}| i - {i}| step1 {step1}| step2 {step2}")
    return min(step1, step2)

# solution 3 - less time, more memory
def min_cost_climbing_stairs3(cost):
    step1, step2 = cost[0], cost[1]
    for i in range(2, len(cost)):
        temp = cost[i] + min(step1, step2)
        step1 = step2
        step2 = temp
        print(f"current_step {temp}| i - {i}| step1 {step1}| step2 {step2}")
    return min(step1, step2)

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]  # 6
print(min_cost_climbing_stairs3(cost))
