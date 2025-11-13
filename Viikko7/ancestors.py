class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def ancestor(node, a, b):
    if node.value == a and a == b:
        return True
    if node.value == a:
        truth_values = []
        for child in node.children:
            truth_values.append(ancestor(child, None, b))
        return True if True in truth_values else False

    elif node.value == b and a == None:
        return True

    elif len(node.children):
        truth_values = []
        for child in node.children:
            truth_values.append(ancestor(child, a, b))
        return True if True in truth_values else False

    else:
        return False

