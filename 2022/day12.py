filename = "input/day12.txt"    
# filename = "input/day12_sample.txt"

letters = 'abcdefghijklmnopqrstuvwxyz'
dc = {letters[i]:i for i in range(len(letters))}

with open(filename, 'r') as f:
    lines = f.readlines()
    map = [[dc[c] if c in dc.keys() else -1 for c in line.strip()] for line in lines]

# for row in map:
    # print(row)

class Vertex:
    def __init__(self, id, value, height):
        self.id = id
        self.value = value
        self.neighbours = set()
        self.weights = {}
        self.height = height
    
    def addNeigh(self, neigh, weight):
        self.neighbours.add(neigh)
        self.weights[neigh] = weight

    def __str__(self):
        s = f'{self.id} value:{self.value}'
        for neigh in self.neighbours:
            if self.weights[neigh] == 1:
                s+= f'\t{neigh}'
        return s

# build directed graph
# find shortest path in directed graph
graph = {}
for i in range(len(map)):
    for j in range(len(map[0])):
        u = (i, j)
        graph[u] = Vertex(u, map[i][j], map[i][j])
        
        # bottom direction
        if i < len(map) - 1 and map[i][j] - map[i+1][j] >= -1:
            neigh = (i+1, j)
            graph[u].addNeigh(neigh, 1)
        else:
            neigh = (i+1, j)
            graph[u].addNeigh(neigh, float('inf'))
        
        # top direction
        if i > 0 and map[i][j] - map[i-1][j] >= -1:
            neigh = (i-1, j)
            graph[u].addNeigh(neigh, 1)
        else:
            neigh = (i-1, j)
            graph[u].addNeigh(neigh, float('inf'))

        # left direction
        if j > 0 and map[i][j] - map[i][j-1] >= -1:
            neigh = (i, j-1)
            graph[u].addNeigh(neigh, 1)
        else:
            neigh = (i, j-1)
            graph[u].addNeigh(neigh, float('inf'))

        # right direction
        if j < len(map[0]) - 1 and map[i][j] - map[i][j+1] >= -1:
            neigh = (i, j+1)
            graph[u].addNeigh(neigh, 1)
        else:
            neigh = (i, j+1)
            graph[u].addNeigh(neigh, float('inf'))

def dijkstra(graph, s):

    dist = {k:float('inf') for k in graph.keys()}
    queue = set([k for k in graph.keys()])

    dist[s] = 0
    
    while len(queue) > 0:
        # get node with min dist
        mindist = float('inf')
        u = next(iter(queue))
        for v in queue:
            if dist[v] < mindist:
                mindist = dist[v]
                u = v
        queue.remove(u)
        # print(queue)

        for neigh in graph[u].neighbours: 
            if neigh not in queue:
                continue
            newdist = dist[u] + graph[u].weights[neigh]
            if newdist < dist[neigh]:
                dist[neigh] = newdist
    return dist
   
# part 1

starting_point = (0, 0)
endpoint = (0,0)
for i in range(len(map)):
    for j in range(len(map[0])):
        if lines[i][j] == 'E':
            endpoint = (i, j)
            map[i][j] = 25
        
        if lines[i][j] == 'S':
            starting_point = (i, j)
            map[i][j] = 0

dist = dijkstra(graph, starting_point)
print(dist[endpoint])

# part 2

starting_points = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 0:
            starting_points.append((i, j))

import datetime
mindist = float('inf')
print(f"Total potential starting points {len(starting_points)}")
for i, starting_point in enumerate(starting_points):
    if i % 10 == 0:
        print(f"{i}: {datetime.datetime.now()}, current min distance: {mindist}")
    dist = dijkstra(graph, starting_point)
    mindist = min(mindist, dist[endpoint])
print(mindist)