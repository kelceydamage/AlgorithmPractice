from queue import PriorityQueue

class GraphVertex:

    def __init__(self, value, adjacency):
        self.value = value
        # list of tuples: index, weight
        self.adjacency = adjacency
        self.shortestDistanceToSource = float('inf')
        self.parent = None

    def __gt__(self, other):
        if other.value > self.value:
            return True
        return False
    
    def __lt__(self, other):
        if other.value < self.value:
            return True
        return False

class Dijkstra:

    def __init__(self):
        self.completedVertices = set()
        self.priorityQueue = PriorityQueue()

    def run(self, graphArray, sourceVertexIndex):
        graphArray[sourceVertexIndex].shortestDistanceToSource = 0
        self.populateQueue(graphArray)

        while not self.priorityQueue.empty():
            _, minVertex = self.priorityQueue.get()
            self.completedVertices = self.completedVertices.union({minVertex})
            for index, edgeWeight in minVertex.adjacency:
                self.relax(minVertex, graphArray[index], edgeWeight)

    def relax(self, minVertex, adjacentVertex, edgeWeight):
        if adjacentVertex.shortestDistanceToSource > minVertex.shortestDistanceToSource + edgeWeight:
            adjacentVertex.shortestDistanceToSource = minVertex.shortestDistanceToSource + edgeWeight
            adjacentVertex.parent = minVertex
            self.priorityQueue.put((adjacentVertex.shortestDistanceToSource, adjacentVertex))

    def populateQueue(self, graphArray):
        [self.priorityQueue.put((vertex.shortestDistanceToSource, vertex)) for vertex in graphArray]   

    def printResults(self):
        shortestPathResultString = ', '.join(
            [f"{v.value}={v.shortestDistanceToSource}" for v in self.completedVertices]
        )
        print(f'Shortest paths to {graphArray[0].value}: {shortestPathResultString}')


if __name__ == "__main__":
    graphArray = [
        GraphVertex('a', [(1, 5), (3, 17)]),
        GraphVertex('b', [(0, 5), (2, 3), (4, 6), (5, 13)]),
        GraphVertex('c', [(1, 3), (3, 5), (5, 1)]),
        GraphVertex('d', [(0, 17), (2, 5), (4, 2)]),
        GraphVertex('e', [(1, 6), (3, 2), (5, 4)]),
        GraphVertex('f', [(1, 13), (2, 1), (4, 4)])
    ]
    D = Dijkstra()
    D.run(graphArray, 0)
    D.printResults()
    
