class Node(object):
    """ Assume name as a string """
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    """ Assume src and dest are Node object"""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest   
    def getSrc(self):
        return self.src    
    def getDest(self):
        return self.dest
    def __str__(self):
        return f"{self.src} -> {self.dest}"
    
class Diagraph(object):
    """ edges is dict mapping ich node to list of it's child """
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node  in self.edges:
            raise ValueError("Duplicate Node")
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSrc()
        dest = edge.getDest()
        if not (src in self.edges and dest in self.edges):
            raise ValueError("Nodes for this edge doesn't exist in the diagraph")
        self.edges[src].append(dest)
    def childrenOf(self, node):
        if node in self.edges:
            return self.edges[node]
        raise ValueError("This node doesn't exist in our diagraph")
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for node in self.edges:
            if node.getName() == name:
                return node
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + "->"\
                    + dest.getName() + "\n"
        return result[:-1] # omit final line


class Graph(Diagraph):
    def addEdge(self, edge):
        Diagraph.addEdge(self, edge)
        revEdge = Edge(edge.getDest(), edge.getSrc())
        Diagraph.addEdge(self, revEdge)


def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


def DFS(graph, start, end, path, shortest, toPrint=False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path += [start]
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
    return shortest
            
    


# testSP('Chicago', 'Boston')
# print()
# testSP('Boston', 'Phoenix')
# print()

printQueue = True 

def BFS(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        curPath = pathQueue.pop(0)
        if curPath[-1] == end:
            return curPath
        for node in graph.childrenOf(start):
            if node not in curPath:
                initPath += [node]
                pathQueue.append(pathQueue)
    return None

def shortestPath(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end, toPrint)
    
# testSP('Boston', 'Phoenix')

