from graph import ListGraph

class BFSGraph(ListGraph):
    """ Implementation of a breadth-first search.

    Args:
        ListGraph (_type_): Parent class ListGraph is an adjacency list graph.
    """
    def __init__(self, node_count: int) -> None:
        super().__init__(node_count)

    def bfs(self):
        pass

if __name__ == "__main__":
    pass