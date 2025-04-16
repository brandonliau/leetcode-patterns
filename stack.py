# Generic setup for monotonic increasing stack
def monotonic_increasing_stack(input: list):
    stack = [] 
    for val in input:
        while stack and stack[-1] > val:
            val = stack.pop() 
        stack.append(val)
    return

# Generic setup for monotonic decreasing stack
def monotonic_decreasing_stack(input: list):
    stack = []
    for val in input:
        while stack and stack[-1] < val:
            temp = stack.pop()
            # PROCESS temp
        stack.append(val)
    return