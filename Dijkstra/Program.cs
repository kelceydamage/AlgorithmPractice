namespace GraphTools
{
    public class GraphVertex
    {
        public string Value;
        public List<Tuple<int, int>> Adjacency;
        public int ShortestDistanceToSource = int.MaxValue;
        public GraphVertex? Parent = null;

        public GraphVertex(string value, List<Tuple<int, int>> adjacency)
        {
            Value = value;
            Adjacency = adjacency;
        }
    }

    public class Dijkstra
    {
        private PriorityQueue<GraphVertex, int> priorityQueue = new();
        public HashSet<GraphVertex> completedVertices = new();
        private int sourceIndex = 0;

        public void Run(List<GraphVertex> graphArray, int sourceVertexIndex)
        {
            sourceIndex = sourceVertexIndex;
            graphArray[sourceIndex].ShortestDistanceToSource = 0;
            PopulateQueue(graphArray);

            while (priorityQueue.Count != 0)
            {
                GraphVertex minVertex = priorityQueue.Dequeue();
                completedVertices.UnionWith(new HashSet<GraphVertex> {minVertex});
                foreach (Tuple<int, int> adjacencyTuple in minVertex.Adjacency)
                {
                    Relax(minVertex, graphArray[adjacencyTuple.Item1], adjacencyTuple.Item2);
                }
            }
        }

        public void PrintResults()
        {
            foreach (GraphVertex vertex in completedVertices)
            {
                Console.WriteLine($"Path to {sourceIndex}: {vertex.Value}={vertex.ShortestDistanceToSource}");
            }
        }

        private void PopulateQueue(List<GraphVertex> graphArray)
        {
            foreach (GraphVertex vertex in graphArray)
            {
                priorityQueue.Enqueue(vertex, vertex.ShortestDistanceToSource);
            }
        }

        private void Relax(GraphVertex minVertex, GraphVertex adjacentVertex, int weight)
        {
            if (adjacentVertex.ShortestDistanceToSource > minVertex.ShortestDistanceToSource + weight)
            {
                adjacentVertex.ShortestDistanceToSource = minVertex.ShortestDistanceToSource + weight;
                adjacentVertex.Parent = minVertex;
                priorityQueue.Enqueue(adjacentVertex, adjacentVertex.ShortestDistanceToSource);
            }
        }
    }

    public class Program
    {
        public static void Main()
        {
            List<GraphVertex> graphArray = new() {
                new GraphVertex("A", new List<Tuple<int, int>> {
                    Tuple.Create(1, 5),
                    Tuple.Create(3, 17),
                }),
                new GraphVertex("B", new List<Tuple<int, int>> {
                    Tuple.Create(0, 5),
                    Tuple.Create(2, 3),
                    Tuple.Create(4, 6),
                    Tuple.Create(5, 13),
                }),
                new GraphVertex("C", new List<Tuple<int, int>> {
                    Tuple.Create(1, 3),
                    Tuple.Create(3, 5),
                    Tuple.Create(5, 1),
                }),
                new GraphVertex("D", new List<Tuple<int, int>> {
                    Tuple.Create(0, 17),
                    Tuple.Create(2, 5),
                    Tuple.Create(4, 2),
                }),
                new GraphVertex("E", new List<Tuple<int, int>> {
                    Tuple.Create(1, 6),
                    Tuple.Create(3, 2),
                    Tuple.Create(5, 4),
                }),
                new GraphVertex("F", new List<Tuple<int, int>> {
                    Tuple.Create(1, 13),
                    Tuple.Create(2, 1),
                    Tuple.Create(4, 4),
                }),
            };

            Console.WriteLine(graphArray);
            Dijkstra D = new();
            D.Run(graphArray, 0);
            D.PrintResults();
        }
    }
}
