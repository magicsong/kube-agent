class KubernetesGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, resource_name, resource_type):
        self.nodes[resource_name] = resource_type
        if resource_name not in self.edges:
            self.edges[resource_name] = []

    def add_edge(self, from_resource, to_resource):
        if from_resource in self.edges and to_resource in self.nodes:
            self.edges[from_resource].append(to_resource)

    def get_neighbors(self, resource_name):
        return self.edges.get(resource_name, [])

    def display_graph(self):
        for node in self.nodes:
            print(f"{node} ({self.nodes[node]}): {self.get_neighbors(node)}")

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.edges:
            return None
        for node in self.edges[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath
        return None

    def clear_graph(self):
        self.nodes.clear()
        self.edges.clear()