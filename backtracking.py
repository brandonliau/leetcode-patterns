def condition(curr: list):
    return

# Generic setup for backtracking
def backtracking(data: list):
    curr, ans = [], []
    def backtrack(candidate: int):
        if condition(curr):
            ans.append(curr.copy())
            return
        curr.append(data[candidate])
        backtrack(data, candidate, curr, ans)
        curr.pop()
        backtrack(data, candidate + 1, curr, ans)
    backtrack(0)
    return