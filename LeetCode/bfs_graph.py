from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, source, destination):
        self.graph[source].append(destination)

    def BFS(self, source):
        visited = {key: False for key in self.graph.keys()}
        queue = []

        queue.append(source)
        visited[source] = True

        while queue:
            s = queue.pop(0)
            print(s)

            for i in self.graph[s]:
                if not visited.get(i, False):
                    queue.append(i)
                    visited[i] = True

# a = Graph()
# a.add_edge("a", "b")
# a.add_edge("a", "c")

# a.add_edge("b", "d")
# a.add_edge("b", "e")

# a.add_edge("c", "f")
# a.add_edge("c", "g")

# a.BFS("b")


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.BFS(2)
