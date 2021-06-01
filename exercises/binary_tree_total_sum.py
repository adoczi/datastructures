# The input it the root node
# Return the total sum of the node values in a Binary Tree
#
#       3
#      /  \
#     2    7
#    / \    \
#   4  -2    5
#

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return "Node: {} Left: {} Right:{}".format(self.val, self.left, self.right)

    def visit(self):
        print(self.val, end='')


def depth_first_sum(root_node):
    stack = [root_node]
    counter = 0

    while len(stack) > 0:

        current_node = stack.pop()
        counter += current_node.val

        if current_node.right is not None:
            stack.append(current_node.right)

        if current_node.left is not None:
            stack.append(current_node.left)

    return counter


def depth_first_sum_recursive(root_node):
    if root_node is None:
        return 0
    return root_node.val + depth_first_sum_recursive(root_node.left) + depth_first_sum_recursive(root_node.right)


a = Node(3)
b = Node(2)
c = Node(7)
d = Node(4)
e = Node(-2)
f = Node(5)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print("Depth First Sum Iteratively: {}".format(depth_first_sum(a)))
print("Depth First Sum Recursively: {}".format(depth_first_sum_recursive(a)))