from typing import List


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def tree_traversal(n: int, nodes: List[List[str]]) -> List[str]:
    node_dict = dict()
    node_dict[None] = None

    for element in nodes:
        value, left, right = element
        if left == ".":
            left = None
        if right == ".":
            right = None

        node = Node(value, left, right)
        node_dict[node.value] = node

    pre_order_result = ""
    in_order_result = ""
    post_order_result = ""

    def pre_order(root: Node):
        nonlocal node_dict, pre_order_result
        if root is None:
            return

        pre_order_result += root.value
        pre_order(node_dict[root.left])
        pre_order(node_dict[root.right])

    def in_order(root: Node):
        nonlocal node_dict, in_order_result
        if root is None:
            return

        in_order(node_dict[root.left])
        in_order_result += root.value
        in_order(node_dict[root.right])

    def post_order(root: Node):
        nonlocal node_dict, post_order_result
        if root is None:
            return

        post_order(node_dict[root.left])
        post_order(node_dict[root.right])
        post_order_result += root.value

    pre_order(node_dict["A"])
    in_order(node_dict["A"])
    post_order(node_dict["A"])

    return [pre_order_result, in_order_result, post_order_result]
