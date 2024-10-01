from dfs import DFSGraph

class GraphTester:
    def __init__(self) -> None:
        pass

    def build_graph(self):
        node_count = int(input("How many nodes?\n"))

        g = DFSGraph(node_count)

        edge = input("Give an edge as: x, y or enter nothing to run DFS.\n")
        while(edge != ''):
            nodes = edge.split(' ')
            if len(nodes) != 2:
                raise Exception('Invalid arguments for edge.')
            
            node_1, node_2 = 0, 0
            try:
                node_1 = int(nodes[0])
                node_2 = int(nodes[1])
            except Exception:
                raise Exception('Argument not an integer.')
            g.add_edge(node_1, node_2)
            edge = input("Give an edge as: x, y or enter nothing to run DFS.\n")

        source = int(input('Starting source node?\n'))
        g.dfs(source)

if __name__ == "__main__":
    g = GraphTester()
    g.build_graph()