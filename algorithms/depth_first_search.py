# DFS is preferred if we want to visit evey node in a graph
# it is told to be simpler than breadth first search

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return "Node: {} Left: {} Right:{}".format(self.val, self.left, self.right)

    def visit(self):
        print(self.val, end='')


# n == number of nodes
# O(n) time
# O(n) space
def depth_first_search(root_node):
    stack = [root_node]

    while len(stack) > 0:

        current_node = stack.pop()
        current_node.visit()

        if current_node.right is not None:
            stack.append(current_node.right)

        if current_node.left is not None:
            stack.append(current_node.left)


# O(n) time and O(n) space where n == number of nodes
# pre-order depth search traversal: print myself, then left then right
def depth_first_search_recursive(root):
    if root is None:
        return
    root.visit()
    depth_first_search_recursive(root.left)
    depth_first_search_recursive(root.right)


# in-order depth search traversal: print left then myself then right
def depth_first_search_recursive_in(root):
    if root is None:
        return
    depth_first_search_recursive_in(root.left)
    root.visit()
    depth_first_search_recursive_in(root.right)


# post-order depth search traversal: print left then right then myself
def depth_first_search_recursive_post(root):
    if root is None:
        return
    depth_first_search_recursive_post(root.left)
    depth_first_search_recursive_post(root.right)
    root.visit()

#
#     a
#    /  \
#   b    c
#  / \    \
# d   e    f


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print("Depth First Search Iteratively: ", end='')
depth_first_search(a)
print()

print("Depth First Search Recursively Pre-order: ", end='')
depth_first_search_recursive(a)
print()

print("Depth First Search Recursively In-order: ", end='')
depth_first_search_recursive_in(a)
print()

print("Depth First Search Recursively Post-order: ", end='')
depth_first_search_recursive_post(a)
print()