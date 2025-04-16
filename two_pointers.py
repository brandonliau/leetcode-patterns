def move_left():
    return

def move_right():
    return

# Generic setup for two pointers
def two_pointers(input: list):
    left, right = 0, len(input) - 1
    while left < right:
        # PROCESS input[left] AND input[right]
        if move_left():
            left += 1
        elif move_right():
            right -= 1
    return