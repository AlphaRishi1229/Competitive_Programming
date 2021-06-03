class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def traverse_nodes(node: Node):
    print(node)
    if not node:
        return node
    if node.left:
        left_val = traverse_nodes(node.value)
    if node.right:
        right_val = traverse_nodes(node.value)
    return node.value + left_val + right_val


def sum_of_nodes(node: Node):
    if not node:
        return 0
    l_max = traverse_nodes(node.left)
    r_max = traverse_nodes(node.right)
    return max(
        node.value + l_max + r_max,
        node.value + l_max,
        node.value + r_max,
        node.value
    )

tree = Node(3)

tree.left = Node(4)
tree.left.left = Node(-10)
tree.left.right = Node(4)

tree.right = Node(5)

print(sum_of_nodes(tree))
