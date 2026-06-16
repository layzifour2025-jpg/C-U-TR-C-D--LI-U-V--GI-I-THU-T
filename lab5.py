from collections import deque

def build_graph(edges, directed=False):
    graph = {}
    for u, v in edges:
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph

def bfs(graph, start):
    if start not in graph: return []
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

def dfs_recursive(graph, start, visited=None, result=None):
    if visited is None: visited = set()
    if result is None: result = []
    if start not in graph: return result
    visited.add(start)
    result.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)
    return result

def count_connected_components(graph):
    visited = set()
    components = []
    def bfs_component(start_node):
        queue = deque([start_node])
        visited.add(start_node)
        component = []
        while queue:
            vertex = queue.popleft()
            component.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return component
    for vertex in graph:
        if vertex not in visited:
            components.append(bfs_component(vertex))
    return len(components), components

def has_cycle_undirected(graph):
    visited = set()
    def dfs(vertex, parent):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if dfs(neighbor, vertex): return True
            elif neighbor != parent:
                return True
        return False
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None): return True
    return False

def has_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {vertex: WHITE for vertex in graph}
    def dfs(vertex):
        color[vertex] = GRAY
        for neighbor in graph.get(vertex, []):
            if color[neighbor] == GRAY: return True
            if color[neighbor] == WHITE:
                if dfs(neighbor): return True
        color[vertex] = BLACK
        return False
    for vertex in graph:
        if color[vertex] == WHITE:
            if dfs(vertex): return True
    return False

def topological_sort_dfs(graph):
    if has_cycle_directed(graph): return None
    visited = set()
    stack = []
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(vertex)
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
    return stack[::-1]

def topological_sort_kahn(graph):
    in_degree = {vertex: 0 for vertex in graph}
    for vertex in graph:
        for neighbor in graph[vertex]:
            if neighbor not in in_degree: in_degree[neighbor] = 0
            in_degree[neighbor] += 1
    queue = deque([v for v in graph if in_degree[v] == 0])
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph.get(vertex, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(result) != len(graph): return None
    return result

def build_course_graph(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    for course, pre in prerequisites:
        graph[pre].append(course)
    return graph

def can_finish(num_courses, prerequisites):
    graph = build_course_graph(num_courses, prerequisites)
    return not has_cycle_directed(graph)

def find_order(num_courses, prerequisites):
    graph = build_course_graph(num_courses, prerequisites)
    order = topological_sort_kahn(graph)
    return order if order is not None else []

if __name__ == "__main__":
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    g_undirected = build_graph(edges, False)
    print("BFS:", bfs(g_undirected, 'A'))
    print("DFS:", dfs_recursive(g_undirected, 'A'))
    
    g_comp = {'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}
    print("TP liên thông:", count_connected_components(g_comp))

    g_undirected_cycle = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    g_directed_cycle = {'A': ['B'], 'B': ['C'], 'C': ['A']}
    print("Chu trình vô hướng:", has_cycle_undirected(g_undirected_cycle))
    print("Chu trình có hướng:", has_cycle_directed(g_directed_cycle))

    dag = {'A': ['C'], 'B': ['C', 'D'], 'C': ['E'], 'D': ['F'], 'E': ['F'], 'F': []}
    print("Topo Sort (Kahn):", topological_sort_kahn(dag))
    
    n = 4
    prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print("Can finish:", can_finish(n, prereqs))
    print("Order:", find_order(n, prereqs))