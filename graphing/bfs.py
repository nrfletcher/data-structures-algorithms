from graph import ListGraph

class BFSGraph(ListGraph):
    """ Implementation of a breadth-first search.

    Args:
        ListGraph (_type_): Parent class ListGraph is an adjacency list graph.
    """
    def __init__(self, node_count: int) -> None:
        super().__init__(node_count)

    def bfs(self, source: int):
        
        visited = [0 for i in range(len(self.edges))]
        queue = []
        queue.append(source)

        while len(queue) > 0:
            node = queue.pop(0)

            if not visited[node]:
                print(node)
                visited[node] = 1

            for neighbor in self.edges[node]:
                if visited[neighbor] == 0:
                    queue.append(neighbor)

if __name__ == "__main__":
    g = BFSGraph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(1, 2)
    g.bfs(0)