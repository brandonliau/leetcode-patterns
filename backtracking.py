def condition(curr: list):
    return

# Generic setup for backtracking
def backtrack(data: list, candidate: int, curr: list, ans: list):
    if condition(curr):
        ans.append(curr.copy())
        return
    curr.append(data[candidate])
    backtrack(data, candidate + 1, curr, ans)
    curr.pop()
    backtrack(data, candidate + 1, curr, ans)
