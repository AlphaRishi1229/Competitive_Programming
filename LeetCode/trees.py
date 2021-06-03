class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def print_in_order(root: Node):
    if root:
        print_in_order(root.left)
        print(root.value)
        print_in_order(root.right)

def print_pre_order(root: Node):
    if root:
        print(root.value)
        print_pre_order(root.left)
        print_pre_order(root.right)

def print_post_order(root: Node):
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.value)

def print_left_most_tree(root: Node):
    if not root:
        return None

    node_list = [root]
    while len(node_list):
        length = len(node_list)
        for i in range(1, length+1):
            temp = node_list.pop(0)
            if i == 1:
                print(temp.value)
            if temp.left:
                node_list.append(temp.left)
            if temp.right:
                node_list.append(temp.right)

def print_right_most_tree(root: Node):
    if not root:
        return None

    node_list = [root]
    while len(node_list):
        length = len(node_list)
        for i in range(1, length+1):
            temp = node_list.pop(0)
            if i == 1:
                print(temp.value)
            if temp.right:
                node_list.append(temp.right)
            if temp.left:
                node_list.append(temp.left)

def height_of_node(node: Node, current_height: int):
    if not node:
        return 0, 0
    left_height = height_of_node(node.left, current_height)[0]
    right_height = height_of_node(node.right, current_height)[0]
    current_height = max(current_height, 1 + left_height + right_height)
    return 1 + max(left_height, right_height), current_height

def diameter_of_tree(root: Node):
    if not root:
        return 0
    current_diameter = float("-inf")
    height_of_tree, current_diameter = height_of_node(root, current_diameter)
    return current_diameter

a = Node(5)

a.left = Node(3)
a.right = Node(6)

a.left.left = Node(1)
a.left.right = Node(4)
a.left.left.left = Node(2)
a.left.left.right = Node(15)

a.right.left = Node(7)
a.right.right = Node(8)
a.right.right.left = Node(20)
a.right.right.right = Node(12)

"""
Tree:
            5
          /   \
        3       6
      /   \    /  \
    1       4 7     8
   / \             /  \
  2   15          20    12
"""
print("Pre-Order traversal: ")
print_pre_order(a)
print("In-Order traversal: ")
print_in_order(a)
print("Post-Order traversal: ")
print_post_order(a)
print("Left Most Tree")
print_left_most_tree(a)
print("Right Most Tree")
print_right_most_tree(a)
print("Diameter of tree")
print(diameter_of_tree(a))
