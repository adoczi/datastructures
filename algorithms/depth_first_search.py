#!
"""
    a
   /  \
  b    c
 / \    \
d   e    f
"""
def depth_first_search(root_node):
    """
    :param root_node:
    :return:
    """
    stack = []
    while len(stack) > 0:
        current_node = stack.pop()
        print(current_node.value)

        if current_node.right is not None:
            stack.push(current_node.right)

        if current_node.left is not None:
            stack.push(current_node.left)

print depth_first_search(a)

