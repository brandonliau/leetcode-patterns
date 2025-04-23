def condition():
    return

# Generic setup for two pointers
def two_pointers(data: list):
    left, right = 0, len(data) - 1
    while left < right:
        # PROCESS data[left] AND data[right]
        if condition():
            left += 1
        else:
            right -= 1
    return