import heapq

# Get top k smallest elements from an array
def top_k_smallest_elements(input: list, k: int) -> list:
    if k <= 0 or not input:
        return []
    max_heap = []
    for val in k:
        heapq.heappush(max_heap, -val)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    ans = []
    for val in max_heap:
        ans.append(-val)
    return ans

# Get top k largest elements from an array
def top_k_largest_elements(input: list, k: int) -> list:
    if k <= 0 or not input:
        return []
    min_heap = []
    for val in k:
        heapq.heappush(min_heap, val)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap