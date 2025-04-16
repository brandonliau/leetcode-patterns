import collections

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive pre-order dfs
def recursive_preorder_dfs(root: TreeNode):
    if not root:
        return
    # PROCESS NODE
    recursive_preorder_dfs(root.left)
    recursive_preorder_dfs(root.right)

# Recursive in-order dfs
def recursive_inorder_dfs(root: TreeNode):
    if not root:
        return
    recursive_inorder_dfs(root.left)
    # PROCESS NODE
    recursive_inorder_dfs(root.right)

# Recursive post-order dfs
def recursive_postorder_dfs(root: TreeNode):
    if not root:
        return
    recursive_postorder_dfs(root.left)
    recursive_postorder_dfs(root.right)
    # PROCESS NODE

# Iterative pre-order dfs
def iterative_preorder_dfs(root: TreeNode):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        # PROCESS NODE
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return

# Iterative in-order dfs
def iterative_inorder_dfs(root: TreeNode):
    if not root:
        return
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        # PROCESS NODE
        curr = curr.right
    return

# Iterative post-order dfs
def iterative_postorder_dfs(root: TreeNode):
    if not root:
        return
    stack = []
    curr = root
    last_visited = None
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        node = stack[-1]
        if node.right and last_visited != node.right:
            curr = node.right
        else:
            # PROCESS NODE
            stack.pop()
            last_visited = node
    return

# Iterative bfs
def iterative_bfs(root: TreeNode):
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node:
            # PROCESS NODE
            queue.append(node.left)
            queue.append(node.right)
    return