def condition():
    return

# Minimum length of dynamic sliding window
def min_sliding_window(data: list):
    window = []
    left = 0
    minl = 0
    for right in range(len(data)):
        window.append(data[right])
        while condition():
            minl = min(minl, right - left + 1)
            window.remove(data[left])
            left += 1
        # PROCESS ITEMS IN WINDOW
    return

# Maximum length of dynamic sliding window
def max_sliding_window(data: list):
    window = []
    left = 0
    maxl = 0
    for right in range(len(data)):
        window.append(data[right])
        while condition():
            window.remove(data[left])
            left += 1
        # PROCESS ITEMS IN WINDOW
        maxl = max(maxl, right - left + 1)
    return

# Fixed length sliding window
def fixed_sliding_window(data: list, k: int):
    window = []
    left = 0
    for right in range(len(data)):
        window.append(data[right])
        if (right - left + 1) < k:
            continue
        # PROCESS ITEMS IN WINDOW
        window.remove(data[left])
        left += 1
    return