import collections

# Build an adjacency list given an edge list
def build_adjacency_list(edge_list: list) -> dict:
    adj = collections.defaultdict(list)
    for u, v in edge_list:
        adj[u].append(v)
    return adj

# Build an adjacency matrix given an edge list
def build_adjacency_matrix(edge_list: list, n_nodes: int) -> list:
    matrix = []
    for _ in range(n_nodes):
        matrix.append([0] * n_nodes)
    for u, v in edge_list:
        matrix[u][v] = 1
        matrix[v][u] = 1 # comment out this line for directed graphs
    return matrix

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

# Recursive dfs given an adjacency matrix
def recursive_adjacency_matrix_dfs(matrix: list):
    visited = set()
    def dfs(node):
        visited.add(node)
        # PROCESS NODE
        for neighbor in range(len(matrix)):
            if matrix[node][neighbor] and neighbor not in visited:
                dfs(neighbor)
    for node in range(len(matrix)):
        if node not in visited:
            dfs(node)
    return

# Iterative dfs given an adjacency matrix
def recursive_adjacency_matrix_dfs(matrix: list):
    visited = set()
    def dfs(node):
        stack = [node]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                # PROCESS NODE
                for neighbor in range(len(matrix)):
                    if matrix[node][neighbor] and neighbor not in visited:
                        stack.append(neighbor)
    for node in range(len(matrix)):
        if node not in visited:
            dfs(node)
    return

# Iterative bfs given an adjacency matrix
def iterative_adjacency_matrix_bfs(matrix: list):
    visited = set()
    def bfs(node):
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                # PROCESS NODE
                for neighbor in range(len(matrix)):
                    if matrix[node][neighbor] and neighbor not in visited:
                        queue.append(neighbor)
    for node in range(len(matrix)):
        if node not in visited:
            bfs(node)
    return