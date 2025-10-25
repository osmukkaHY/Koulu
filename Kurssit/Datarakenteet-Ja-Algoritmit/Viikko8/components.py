class Components:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def visit(self, node):
        if node in self.components:
            return
        self.components[node] = self.counter

        for next_node in self.graph[node]:
            self.visit(next_node)

    def find_components(self):
        self.counter = 0
        self.components = {}

        for node in self.nodes:
            if node not in self.components:
                self.counter += 1
                self.visit(node)

        return self.components


def find_components(nodes, edges):
    c = Components(nodes)
    components = {}
    for a, b in edges:
        c.add_edge(a, b)
    dct = c.find_components()

    for key in dct:
        value = dct[key]
        if not value in components:
            components[value] = [key]
        else:
            components[value].append(key)
    return sorted([sorted(graph) for graph in components.values()], key=lambda x: x[0])

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(find_components(nodes, edges)) # [[1, 2, 3], [4, 5, 6, 7], [8]]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_components(nodes, edges)) # [[1], [2], [3], [4], [5]]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_components(nodes, edges)) # [[1, 2, 3, 4, 5]]
