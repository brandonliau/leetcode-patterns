# Generic setup for monotonic increasing stack
def monotonic_increasing_stack(data: list):
    stack = [] 
    for val in data:
        while stack and stack[-1] > val:
            val = stack.pop()
            # PROCESS val
        stack.append(val)
    return

# Generic setup for monotonic decreasing stack
def monotonic_decreasing_stack(data: list):
    stack = []
    for val in data:
        while stack and stack[-1] < val:
            val = stack.pop()
            # PROCESS val
        stack.append(val)
    return