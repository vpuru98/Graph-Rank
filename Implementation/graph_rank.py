
class Graph:

    def __init__(self, vertices, edges):
        self.size = len(vertices)
        self.init_mappings(vertices)
        self.init_adjacancy_list(edges)
        self.init_forward_link_counts()

    def init_mappings(self, vertices):
        self.mapping = {}
        self.inverse_mapping = {}
        for i, vertex in enumerate(vertices):
            self.mapping[vertex] = i
            self.inverse_mapping[i] = vertex

    def init_adjacancy_list(self, edges):
        self.adjacancy_list = dict([(i, []) for i in self.inverse_mapping])
        for edge in edges:
            assert edge[0] in self.mapping and edge[1] in self.mapping
            self.adjacancy_list[self.mapping[edge[1]]].append(self.mapping[edge[0]])

    def init_forward_link_counts(self):
        self.forward_links = dict([(i, 0) for i in self.inverse_mapping])
        for vertex_code in self.adjacancy_list:
            for adjacant_vertex_code in self.adjacancy_list[vertex_code]:
                self.forward_links[adjacant_vertex_code] += 1

    def get_sinks(self):
        sinks = []
        for vertex_code in self.forward_links:
            if self.forward_links[vertex_code] == 0 and len(self.adjacancy_list[vertex_code]) > 0:
                sinks.append(vertex_code)
        return sinks

    def get_ranks(self, num_iterations):
        ranks = dict([(i, 1 / self.size) for i in self.inverse_mapping])
        sinks = self.get_sinks()
        d = 0.85
        iteration = 0
        while iteration < num_iterations:
            new_ranks = {}
            for i in self.inverse_mapping:
                new_ranks[i] = ((1 - d) / self.size + d * sum([ranks[adjacant_vertex_code] / self.forward_links
                    [adjacant_vertex_code] for adjacant_vertex_code in self.adjacancy_list[i]]) + d * sum([ranks[sink] /
                        self.size for sink in sinks]))
            ranks = new_ranks
            iteration += 1
        return ranks

    def rank(self, num_iterations=50):
        ranks = self.get_ranks(num_iterations)
        ranking = dict([(self.inverse_mapping[i], ranks[i]) for i in ranks])
        return ranking


if __name__ == '__main__':
    vertices_list = ['A', 'B', 'C', 'D', 'E', 'F', 1, 2, 3, 4, 5]
    edges_list = [('D', 'A'), ('D', 'B'), ('E', 'B'), ('F', 'B'), ('C', 'B'), (1, 'B'), (2, 'B'), (3, 'B'), ('B', 'C'),
                  ('E', 'D'), ('F', 'E'), (1, 'E'), (2, 'E'), (3, 'E'), (4, 'E'), (5, 'E'), ('E', 'F')]
    graph = Graph(vertices_list, edges_list)
    print(graph.rank())
