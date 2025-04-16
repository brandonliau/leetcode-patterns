def condition():
    return

# Minimum length of dynamic sliding window
def min_sliding_window(input: list):
    window = []
    left = 0
    minl = 0
    for right in range(len(input)):
        window.append(input[right])
        while condition():
            minl = min(minl, right - left + 1)
            window.remove(input[left])
            left += 1
        # PROCESS ITEMS IN WINDOW
    return

# Maximum length of dynamic sliding window
def max_sliding_window(input: list):
    window = []
    left = 0
    maxl = 0
    for right in range(len(input)):
        window.append(input[right])
        while condition():
            window.remove(input[left])
            left += 1
        # PROCESS ITEMS IN WINDOW
        maxl = max(maxl, right - left + 1)
    return

# Fixed length sliding window
def fixed_sliding_window(input: list, k: int):
    window = []
    left = 0
    for right in range(len(input)):
        window.append(input[right])
        if (right - left + 1) < k:
            continue
        # PROCESS ITEMS IN WINDOW
        window.remove(input[left])
        left += 1
    return