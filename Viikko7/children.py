class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def count_children(node):
    if node.children == []:
        return [0]

    child_counts = [len(node.children)]
    for child in node.children:
        child_counts += count_children(child)
    return sorted(child_counts)

