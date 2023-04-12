import sys
from typing import Set, Any
from pygame.locals import *
import networkx as nx
import matplotlib.pyplot as plt
def dijkstra(graph, source):
# Khởi tạo một danh sách các đỉnh chưa xét và một dictionary
# để lưu trữ khoảng cách từ nguồn đến từng đỉnh
    unvisited: set[Any] = set(graph.keys())
    distances = {vertex: sys.maxsize for vertex in unvisited}
    distances[source]=0
    predecessor = {vertex: None for vertex in unvisited}

    while unvisited:
        #Lấy đỉnh có khoảng cách từ nguồn ngắn nhất
        current = min(unvisited, key=lambda vertex: distances[vertex])

        #Xóa đỉnh hiện tại khỏi danh sách các đỉnh chưa xét
        unvisited.remove(current)

        #Cập nhật khoảng cách từ nguồn đến các đỉnh kề với đỉnh hiện tại
        for neighbor, weight in graph[current].item():
            distances = distances[current] + weight
            if distances < distances[neighbor]:
                distances[neighbor] = distances
                predecessor[neighbor] = current
    return distances, predecessor

#Vẽ đồ thị trên bảng thư viện networkx và matplotlib
def draw_graph(graph):
    G = nx.DiGraph()
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor, weight=graph[node][neighbor])

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_egdes(G, pos, width=6)
    nx.draw_networkx_labels(G, pos, edge_labels = edge_labels)

    plt.axis('off')
    plt.show()

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
#ví dụ về một đồ thị ngắn có hướng và trọng số
graph = {
    'a': {'b': 3, 'c': 4, 'd': 7},
    'b': {'c': 1, 'f': 5},
    'c': {'f': 6, 'd': 2},
    'd': {'e': 3, 'g': 6},
    'e': {'g': 3, 'h': 4},
    'f': {'e': 1, 'h': 8},
    'g': {'h': 2},
    'h': {'g': 2}
}

draw_graph(graph)

#Tìm đường đi ngắn nhất từ đỉnh 'a' đến các đỉnh còn lại
distances, predecessor = dijkstra(graph,'a')
print(distances)
#output: {'h':13, 'b': 3, 'e':9, 'c': 4, 'g': 12, 'f': 8, 'd': 6, 'a': 0}
#in ra đường đi ngắn nhất từ đỉnh 'a' đến các đỉnh còn lại
print(find_path(graph, 'a','h'))
#output: ['a', 'b', 'f', 'h']