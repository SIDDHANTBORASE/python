from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insertion(root, value):
    if root is None:
        return Node(value)
    if value <= root.data:
        root.left = insertion(root.left,value)
    if value > root.data:
        root.right = insertion(root.right, value)
    
    return root
    
    
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
Nodecount = int(input("Enter the Number of Nodes: "))
while Nodecount-1 != 0:
    value=int(input("Enter the Node Value: "))
    insertion(root, value)
    Nodecount= Nodecount - 1
    
    
print("\nDFS Traversal:")
dfs(root)

print("\nBFS Traversal:")
bfs(root)
