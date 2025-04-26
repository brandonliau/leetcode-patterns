import collections

# Build an adjacency list given an edge list
def build_adjacency_list(edge_list: list) -> dict:
    adj = collections.defaultdict(list)
    for u, v in edge_list:
        adj[u].append(v)
    return adj

# Recursive dfs given an adjacency list
def recursive_adjacency_list_dfs(adj: dict):
    visited = set()
    def dfs(node):
        visited.add(node)
        # PROCESS NODE
        for neighbor in adj.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
    for node in adj:
        if node not in visited:
            dfs(node)
    return

# Iterative dfs given an adjacency list
def iterative_adjacency_list_dfs(adj: dict):
    visited = set()
    def dfs(node):
        stack = [node]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                # PROCESS NODE
                for neighbor in adj.get(node, []):
                    stack.append(neighbor)
    for node in adj:
        if node not in visited:
            dfs(node)
    return

# Iterative bfs given an adjacency list
def iterative_adjacency_list_bfs(adj: dict):
    visited = set()
    def bfs(node):
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                # PROCESS NODE
                for neighbor in adj.get(node, []):
                    queue.append(neighbor)
    for node in adj:
        if node not in visited:
            bfs(node)
    return

# Topological sort given an adjacency list
def adjacency_list_topological_sort(adj: dict):
    visited, curr = set(), set()
    topo = []
    def dfs(node):
        if node in curr:
            return False
        if node in visited:
            return True
        curr.add(node)
        for neighbor in adj.get(node, []):
            if not dfs(neighbor):
                return False
        curr.remove(node)
        visited.add(node)
        topo.append(node)
        return True
    for node in adj:
        if node not in visited:
            if not dfs(node):
                return []
    return topo