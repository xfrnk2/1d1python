from typing import List, Tuple


class TreeNode:
    def __init__(self, number):
        self.number = number
        self.child = []
        self.parent = None

    @property
    def count_child(self):
        return len(self.child)


def get_visit_count(tree_node):
    count = len(tree_node.child)
    for child_node in tree_node.child:
        count += get_visit_count(child_node)
    return count


def initialize_node_dict(nodes: List[Tuple[int, int]]) -> Tuple[dict, bool]:
    node_dict = dict()
    answer = True

    for node in nodes:
        a, b = node
        if a not in node_dict:
            node_dict[a] = TreeNode(a)
        if b not in node_dict:
            node_dict[b] = TreeNode(b)

        node_dict[a].child.append(node_dict[b])
        if node_dict[b].parent is None:
            node_dict[b].parent = node_dict[a]
        else:
            answer = False
    return node_dict, answer


def check_is_tree(nodes: List[Tuple[int, int]]) -> bool:
    if not nodes:
        return True

    node_dict, answer = initialize_node_dict(nodes)
    if len(node_dict) == 0:
        return True
    elif answer is False:
        return False

    root_node = None
    for v in node_dict.values():
        if v.parent is None:
            if root_node is None:
                root_node = v
            else:
                return False

    if root_node is None:
        return False

    visit_count = 1 + root_node.count_child
    for child_node in root_node.child:
        visit_count += get_visit_count(child_node)
    if visit_count != len(node_dict):
        return False
    return answer
