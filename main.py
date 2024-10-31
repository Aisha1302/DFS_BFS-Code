# D  F  S       C  O  D  E
def dfs(graph, start, goal):
    stack = [[start]]
    while stack:
        path = stack.pop()
        node = path[-1]

        # Check if we've reached the goal
        if node == goal:
            return path

        # Get adjacent nodes and traverse
        adjacent_nodes = graph.get(node, [])
        for node2 in adjacent_nodes:
            if node2 not in path:
                new_path = list(path)
                new_path.append(node2)
                stack.append(new_path)
    # Return None if no path is found
    return None


# B  F  S       C  O  D  E
def bfs(graph, start, goal):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Check if we've reached the goal
        if node == goal:
            return path

        # Get adjacent nodes and traverse
        adjacent_nodes = graph.get(node, [])
        for node2 in adjacent_nodes:
            if node2 not in path:
                new_path = list(path)
                new_path.append(node2)
                queue.append(new_path)
    # Return None if no path is found
    return None




def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start = 'A'
    goal = 'F'

    print("Testing DFS:")
    dfs_path = dfs(graph, start, goal)
    if dfs_path:
        print("Path found by DFS:", " -> ".join(dfs_path))
    else:
        print("No path found by DFS")

    print("\nTesting BFS:")
    bfs_path = bfs(graph, start, goal)
    if bfs_path:
        print("Path found by BFS:", " -> ".join(bfs_path))
    else:
        print("No path found by BFS")

main()
