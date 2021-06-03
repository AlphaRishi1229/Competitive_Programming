from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Create a tree from inorder and preorder traversed values.
def cache_inorder(in_ordered: List):
    """
    Inorder sequence (left, root, right): D B E A F C
    Preorder sequence (root, left, right): A B D E C F
    """
    inorder_index_map = {value: index for index, value in enumerate(in_ordered)}
    return inorder_index_map


def build_tree(in_order_tree: List, pre_order_tree: List, start: int, end: int):
    """
    Inorder sequence (left, root, right): D B E A F C
    Preorder sequence (root, left, right): A B D E C F

    end is len(inorder tree)
    """
    global inorder_index_map, preorder_index
    if start > end:
        return None

    current_node = pre_order_tree[preorder_index]
    preorder_index += 1
    tree_node = Node(current_node)

    # If this node has no children then return tree
    if start == end:
        return tree_node

    # Else index of this node in inorder traversal.
    inorder_index = inorder_index_map[current_node]

    # Using index create left and right subtree
    tree_node.left = build_tree(in_order_tree, pre_order_tree, start, inorder_index-1)
    tree_node.right = build_tree(in_order_tree, pre_order_tree, inorder_index+1, end)
    return tree_node

def build_tree_test(in_ordered, pre_ordered, start_index, end_index):
    global inorder_index_map, preorder_index
    if start_index > end_index:
        return None
    current_node = pre_ordered[preorder_index]
    preorder_index += 1
    tree_node = Node(current_node)

    if start_index == end_index:
        # If no children
        return tree_node

    in_ordered_index = inorder_index_map[current_node]
    tree_node.left = build_tree_test(in_ordered, pre_ordered, start_index, in_ordered_index-1)
    tree_node.right = build_tree_test(in_ordered, pre_ordered, in_ordered_index+1, end_index)
    return tree_node


def print_inorder(root: Node):
    if not root:
        return
    print_inorder(root.left)
    print(root.value)
    print_inorder(root.right)


inn = [ 'D', 'B', 'E', 'A', 'F', 'C' ]
pre = [ 'A', 'B', 'D', 'E', 'C', 'F' ]
inorder_index_map = cache_inorder(inn)
preorder_index = 0

print("First")
root1 = build_tree(inn, pre, 0, len(inn)-1)
print_inorder(root1)
preorder_index = 0

print("Second")
root2 = build_tree_test(inn, pre, 0, len(inn)-1)
print_inorder(root2)
