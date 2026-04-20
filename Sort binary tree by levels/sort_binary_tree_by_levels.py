"""
Sort binary tree by levels
"""
def tree_by_levels(node):
    """
    Perform a breadth-first search (BFS) traversal of a binary tree.
    Returns a list of node values level by level, from left to right.
    """
    if node is None:
        return []
    stack = [node]
    res = []
    while stack:
        node = stack.pop(0)
        res.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res
