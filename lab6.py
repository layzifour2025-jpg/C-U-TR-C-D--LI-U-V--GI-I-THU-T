import heapq

def dijkstra(graph, source):
    distances = {v: float('inf') for v in graph}
    distances[source] = 0
    parent = {v: None for v in graph}
    pq = [(0, source)]
    visited = set()
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        if current_dist > distances[u]:
            continue
            
        for v, w in graph[u]:
            new_dist = distances[u] + w
            if new_dist < distances[v]:
                distances[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))
                
    return distances, parent

def reconstruct_path(parent, source, target):
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    if not path or path[0] != source:
        return None
    return path

def print_distances(distances, source):
    print(f"Bảng khoảng cách từ {source}:")
    for v in sorted(distances.keys()):
        d = distances[v]
        if d == float('inf'):
            print(f"  {source} -> {v}: INF (không tới được)")
        else:
            print(f"  {source} -> {v}: {d}")

def test_dijkstra():
    graph = {
        'A': [('B', 4), ('D', 1)],
        'B': [('A', 4), ('C', 2), ('E', 3)],
        'C': [('B', 2), ('F', 5)],
        'D': [('A', 1), ('E', 2)],
        'E': [('D', 2), ('B', 3), ('F', 1)],
        'F': [('E', 1), ('C', 5)]
    }
    source = 'A'
    distances, parent = dijkstra(graph, source)
    
    print_distances(distances, source)
    print("\nĐường đi chi tiết:")
    for v in sorted(graph.keys()):
        if v == source:
            continue
        path = reconstruct_path(parent, source, v)
        if path is None:
            print(f"  {source} -> {v}: không có đường đi")
        else:
            cost = distances[v]
            print(f"  {source} -> {v}: {' -> '.join(path)} (cost = {cost})")


def make_set(vertices):
    parent = {}
    for v in vertices:
        parent[v] = v
    return parent

def find(parent, v):
    steps = 0
    while parent[v] != v:
        v = parent[v]
        steps += 1
    return v, steps

def union(parent, a, b):
    root_a, _ = find(parent, a)
    root_b, _ = find(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a

def make_set_optimized(vertices):
    parent = {}
    size = {}
    for v in vertices:
        parent[v] = v
        size[v] = 1
    return parent, size

def find_optimized(parent, v):
    if parent[v] != v:
        parent[v] = find_optimized(parent, parent[v])
    return parent[v]

def union_optimized(parent, size, a, b):
    root_a = find_optimized(parent, a)
    root_b = find_optimized(parent, b)
    if root_a == root_b:
        return
    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a
    parent[root_b] = root_a
    size[root_a] += size[root_b]

def demo_dsu_basic():
    print("\n=== Demo DSU Basic ===")
    vertices = ['A', 'B', 'C', 'D', 'E']
    parent = make_set(vertices)
    ops = [
        ("union", 'A', 'B'),
        ("union", 'C', 'D'),
        ("find", 'B'),
        ("union", 'B', 'C'),
        ("find", 'D'),
        ("find", 'E'),
    ]
    for op in ops:
        if op[0] == "union":
            _, x, y = op
            print(f"Thực hiện union({x}, {y})")
            union(parent, x, y)
        else:
            _, x = op
            root, _ = find(parent, x)
            print(f"find({x}) = {root}")
        print("  parent hiện tại:", parent)

def compare_basic_vs_optimized():
    print("\n=== So Sánh Basic vs Optimized ===")
    n = 1000
    vertices = list(range(n))
    parent_basic = make_set(vertices)
    parent_opt, size_opt = make_set_optimized(vertices)
    
    for i in range(n - 1):
        union(parent_basic, i, i + 1)
        union_optimized(parent_opt, size_opt, i, i + 1)
        
    _, steps_b1 = find(parent_basic, 0)
    find_optimized(parent_opt, 0)
    print(f"  [Basic] Số bước duyệt lần 1: {steps_b1}")
    
    _, steps_b2 = find(parent_basic, 0)
    print(f"  [Basic] Số bước duyệt lần 2: {steps_b2}")
    print("  [Optimized] Đã nén phẳng cấu trúc, các lần sau chỉ tốn ~ O(1)")


def kruskal_mst_basic(vertices, edges):
    edges_sorted = sorted(edges, key=lambda e: e[0])
    parent = make_set(vertices)
    mst = []
    total_weight = 0
    
    print("Cạnh sau khi sort (w, u, v):")
    for e in edges_sorted:
        print("  ", e)
        
    print("\nDuyệt từng cạnh:")
    for w, u, v in edges_sorted:
        root_u, _ = find(parent, u)
        root_v, _ = find(parent, v)
        print(f"Xét cạnh {u}-{v} (w={w}), root_u={root_u}, root_v={root_v}")
        
        if root_u != root_v:
            print("  -> Khác nhóm => CHỌN cạnh này")
            mst.append((u, v, w))
            total_weight += w
            union(parent, u, v)
        else:
            print("  -> Cùng nhóm => BỎ")
            
        if len(mst) == len(vertices) - 1:
            break
    return mst, total_weight

def kruskal_mst_optimized(vertices, edges):
    edges_sorted = sorted(edges, key=lambda e: e[0])
    parent, size = make_set_optimized(vertices)
    mst = []
    total_weight = 0
    
    for w, u, v in edges_sorted:
        if find_optimized(parent, u) != find_optimized(parent, v):
            mst.append((u, v, w))
            total_weight += w
            union_optimized(parent, size, u, v)
            if len(mst) == len(vertices) - 1:
                break
    return mst, total_weight

def test_kruskal():
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        (1, 'A', 'B'),
        (4, 'A', 'C'),
        (3, 'B', 'C'),
        (2, 'B', 'D'),
        (5, 'C', 'E'),
        (2, 'D', 'E'),
    ]
    
    print("\n=== Kruskal với DSU basic ===")
    mst1, total1 = kruskal_mst_basic(vertices, edges)
    print("\nMST basic:")
    for u, v, w in mst1:
        print(f"  {u}-{v} (w={w})")
    print("Tổng trọng số:", total1)
    
    print("\n=== Kruskal với DSU optimized ===")
    mst2, total2 = kruskal_mst_optimized(vertices, edges)
    print("\nMST optimized:")
    for u, v, w in mst2:
        print(f"  {u}-{v} (w={w})")
    print("Tổng trọng số:", total2)


if __name__ == "__main__":
    print("================ RUNNING LAB 6 ================")
    test_dijkstra()
    demo_dsu_basic()
    compare_basic_vs_optimized()
    test_kruskal()
    print("===============================================")