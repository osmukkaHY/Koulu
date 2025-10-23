class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def count_subtrees(node):
    if node.children == []:
        return [1]

    subtree_counts = []
    for child in node.children:
        subtree_counts += count_subtrees(child)
    subtree_counts.append(len(subtree_counts)+1)

    return sorted(subtree_counts)

