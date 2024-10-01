from graph import ListGraph

class DFSGraph(ListGraph):
    def __init__(self, node_count: int) -> None:
        super().__init__(node_count)
        
    def dfs(self, source: int):
        """ Depth-first traversal of a graph data structure using an iterative stack approach.

        Args:
            source (int): our starting node
        """
        visited = [0 for i in range(len(self.edges))]
        stack = []
        stack.append(source)

        while len(stack) > 0:
            node = stack.pop()

            if not visited[node]:
                visited[node] = 1
                print(node)

            for val in self.edges[node]:
                if visited[val] == 0:
                    stack.append(val)
                

if __name__ == "__main__":
    # Create a graph with 10 nodes
    g = DFSGraph(10)

    # Add edges to create a more complex structure
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(3, 7)
    g.add_edge(4, 7)
    g.add_edge(5, 8)
    g.add_edge(6, 8)
    g.add_edge(7, 9)
    g.add_edge(8, 9)

    # Perform DFS starting from node 0
    print("DFS starting from node 0:")
    g.dfs(0)

    # Perform DFS starting from node 5
    print("\nDFS starting from node 5:")
    g.dfs(5)

    # Add some cycles to make it more interesting
    g.add_edge(4, 1)
    g.add_edge(6, 2)
    g.add_edge(9, 0)

    print("\nDFS with cycles, starting from node 0:")
    g.dfs(0)