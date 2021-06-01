class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return "Node: {} Left: {} Right:{}".format(self.val, self.left, self.right)

    def visit(self):
        print(self.val, end='')


def breadth_first_search(root, target):
    queue = [root]
    while len(queue) > 0:
        curr = queue.pop(0)
        # curr.visit()
        if curr.val == target:
            return True
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)
    return False
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

print("Does the tree contein 'e'? ", end='')
print(breadth_first_search(a, 'e'))
print("Does the tree contein 'z'? ", end='')
print(breadth_first_search(a, 'z'))