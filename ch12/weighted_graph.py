class Node(object):
    def __init__(self, name):
        """nameは文字列とする"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """srcとdestはどちらもNodeオブジェクトとする"""
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        """srcとdestは、Nodeオブジェクトであるとし、weightは数とする"""
        self.src = src
        self.dest = dest
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.src.getName() + '->(' + str(self.weight) + ')' \
               + self.getName()


class Digraph(object):
    # nodesはNodeオブジェクトのリストである
    # edgesは書くnodeを、そのnodeの子ノードのリストにマップする辞書である
    def __init__(self):
        self.nodes = []
        self.edges = ()

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' \
                         + dest.getName() + '\n'
        return result[:-1] #最後の改行を省略する

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def printPath(path):
    """path は Nodeオブジェクトからなるリストとする"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result

def DFS(graph, start, end, path, shortest, toPrint = False):
    """graphはDigraphオブジェクト，startとendはNodeオブジェクト，
       pathとshortestは，Nodeオブジェクトのリストとする．
       graphでの，startノードからendノードへの最短路を返す"""
    path = path + [start]
    if toPrint:
        print('Current DFS path:',printPath(path))
    if start  ==  end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #サイクルを避ける
            if shortest  ==  None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
    return shortest

def shortestPath(graph, start, end, toPrint = False):
    """graphはDigraphオブジェクト，startとendはNodeオブジェクトとする．
       graphでの，startノードからendノードへの最短路を返す"""
    return DFS(graph, start, end, [], None, toPrint)


def testSP():
    nodes = []
    for name in range(6): #6つのノードを生成する
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    sp = shortestPath(g, nodes[0], nodes[5], toPrint = True)
    print('Shortest path found by DFS:', printPath(sp))


def BFS(graph, start, end, toPrint = False):
    """graphはDigraphオブジェクト，startとendはNodeオブジェクトとする．
       graphでの，startノードからendノードへの最短路を返す"""
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        #pathQueueの中で1番古い要素を参照し，それを取り除く
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode  ==  end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None