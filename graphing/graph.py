class ListGraph:
    """ Implementation of adjacency list based graph structure
    """
    def __init__(self, node_count: int) -> None:
        self.edges = [[] for _ in range(node_count)]

    def add_edge(self, a: int, b: int) -> None:
        if b >= len(self.edges) or a >= len(self.edges):
            raise Exception('Not a valid node index (we start at 0).')
        if b in self.edges[a] or a in self.edges[b]:
            return
        self.edges[a].append(b)
        self.edges[b].append(a)

    def show_edges(self) -> None:
        for i, node in enumerate(self.edges):
            for edge in node:
                print(f'({i}, {edge})')


class MatrixGraph:
    """ Implementation of matrix list based graph structure
    """
    def __init__(self, node_count: int) -> None:
        self.edges = [[0 for _ in range(node_count)] for _ in range(node_count)] 

    def add_edge(self, a: int, b: int):
        if b >= len(self.edges) or a >= len(self.edges):
            raise Exception('Invalid node, outside range.')
        self.edges[a][b] = 1
        self.edges[b][a] = 1
    
    def show_edges(self):
        for i, row in enumerate(self.edges):
            for j in row:
                if j == 1:
                    print(f'({i}, {j})')

    def show_graph(self):
        for row in self.edges:
            print(row)


def list_test():
    graph = ListGraph(3)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(2, 1)
    graph.show_edges()

if __name__ == "__main__":
    graph = MatrixGraph(3)
    graph.add_edge(0, 1)
    graph.show_graph()
    graph.show_edges()