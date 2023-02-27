from create_graph import *


def clean(nodes, graph, end_node):
    for i in range(nodes):
        if end_node in graph[i]:
            graph[i].remove(end_node)
            graph[i].insert(0, end_node)
    return graph


def shortest_path(predecessor_nodes, start_node, end_node):
    path = [end_node]
    current_node = end_node
    while current_node != start_node:
        current_node = predecessor_nodes[current_node]
        path.append(current_node)
    path.reverse()
    return path


def bfs_shortest_path(graph, start_node, end_node):
    visited_nodes = []
    queue = [start_node]
    predecessor_nodes = {}

    # Problem
    # The problem here is the algorithm looks for the end note by looking at the first element in the queue,
    # and exits the queue even if that is not the most efficient path
    # Solution 1
    # I could resolve this by placing the end node at the beginning of every list so that if the end node is anywhere
    # in that neighbors list, it will go towards the end.

    while queue:
        current_node = queue.pop(0)
        visited_nodes.append(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                queue.append(neighbor)
                predecessor_nodes[neighbor] = current_node
    print(shortest_path(predecessor_nodes, start_node, end_node))


def main():
    nodes = 5
    while True:
        # graph = create_graph(nodes, False)
        graph = {0: [1, 2, 3, 4], 1: [0], 2: [0, 4], 3: [0], 4: [0, 2]}
        start_node = 0
        end_node = 4
        graph = clean(nodes, graph, end_node)
        print(graph)

        bfs_shortest_path(graph, start_node, end_node)
        print(f'Start = {start_node}, End = {end_node}\n')
        draw_graph(nodes, graph)


if __name__ == '__main__':
    main()
