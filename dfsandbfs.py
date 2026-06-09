from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def dfs(root):
    if root is None:
        return
    print(root.data, end="  ")
    dfs(root.left)
    dfs(root.right)
    
def bfs(root):
    if root is None:
        return
    q = deque([root])
    
    while q:
        node= q.popleft()
        print(node.data, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

root_value = int(input("Enter the Root: "))
root = Node(root_value)

queue = deque([root])

while queue:
    current = queue.popleft()
    
    left = int(input(f"Enter left child of {current.data} (-1 for no child): "))
    if left != -1:
        current.left = Node(left)
        queue.append(current.left)

    right = int(input(f"Enter right child of {current.data} (-1 for no child): "))
    if right != -1:
        current.right = Node(right)
        queue.append(current.right)

print("\nDFS Traversal:")
dfs(root)

print("\nBFS Traversal:")
bfs(root)
