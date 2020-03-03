
class Graph:

    def __init__(self, vertices, edges):
        self.size = len(vertices)
        self.init_mappings(vertices)
        self.init_adjacancy_list(edges)


    def init_mappings(self, vertices):
        self.mapping = {}
        self.inverse_mapping = {}
        for i, vertex in enumerate(vertices):
            self.mapping[vertex] = i
            self.inverse_mapping[i] = vertex

    def init_adjacancy_list(self, edges):
        self.adjacancy_list = dict([(i, {'forward_weight_sum': 0, 'in_links': 0, 'out_links': 0, 'adjacancies': {}}) 
            for i in self.inverse_mapping])
        for edge in edges:
            assert edge[0] in self.mapping and edge[1] in self.mapping
            if self.mapping[edge[0]] not in self.adjacancy_list[self.mapping[edge[1]]]['adjacancies']:
                self.adjacancy_list[self.mapping[edge[1]]]['adjacancies'][self.mapping[edge[0]]] = [float(edge[2])]
            else:
                self.adjacancy_list[self.mapping[edge[1]]]['adjacancies'][self.mapping[edge[0]]].append(float(edge[2]))
            self.adjacancy_list[self.mapping[edge[0]]]['forward_weight_sum'] += float(edge[2])
            self.adjacancy_list[self.mapping[edge[1]]]['in_links'] += 1
            self.adjacancy_list[self.mapping[edge[0]]]['out_links'] += 1

    def get_sinks(self):
        sinks = []
        for vertex in self.adjacancy_list:
            if self.adjacancy_list[vertex]['in_links'] > 0 and self.adjacancy_list[vertex]['out_links'] == 0:
                sinks.append(vertex)
        return sinks

    def get_ranks(self, num_iterations, d):
        ranks = dict([(i, 1 / self.size) for i in self.inverse_mapping])
        sinks = self.get_sinks()
        iteration = 0
        while iteration < num_iterations:
            new_ranks = {}
            for i in self.inverse_mapping:
                random_jump_contrib = (1 - d) / self.size
                sink_contrib = d * sum([ranks[sink] / self.size for sink in sinks])
                adjacancy_contrib = d * sum([ranks[adjacant_vertex_code] * (sum(self.adjacancy_list[i]
                    ['adjacancies'][adjacant_vertex_code]) / self.adjacancy_list[adjacant_vertex_code]
                    ['forward_weight_sum']) for adjacant_vertex_code in self.adjacancy_list[i]['adjacancies']])
                new_ranks[i] = random_jump_contrib + sink_contrib + adjacancy_contrib
            ranks = new_ranks
            iteration += 1
        return ranks

    def rank(self, num_iterations=50, d=0.85):
        ranks = self.get_ranks(num_iterations, d)
        ranking = dict([(self.inverse_mapping[i], ranks[i]) for i in ranks])
        return ranking


if __name__ == '__main__':
    vertices_list = ['A', 'B', 'C', 'D', 'E', 'F', 1, 2, 3, 4, 5]
    edges_list = [('D', 'A', 1), ('D', 'B', 1), ('E', 'B', 1), ('F', 'B', 1), ('C', 'B', 1), (1, 'B', 1), 
        (2, 'B', 1), (3, 'B', 1), ('B', 'C', 1), ('E', 'D', 1), ('F', 'E', 1), (1, 'E', 1), (2, 'E', 1), 
        (3, 'E', 1), (4, 'E', 1), (5, 'E', 1), ('E', 'F', 1)]
    graph = Graph(vertices_list, edges_list)
    print(graph.rank())
