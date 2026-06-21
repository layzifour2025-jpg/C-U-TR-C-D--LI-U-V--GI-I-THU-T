import heapq
import sys


def build_graph(edges):
    """
    Input: list of tuples (u, v, cost)
    Output: Adjacency list format {u: [(v, cost), ...]}
    """
    graph = {}
    for u, v, cost in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, cost))
        graph[v].append((u, cost))
        graph[v].append((u, cost))
    return graph


def dijkstra(graph, source):
    """Tìm đường đi ngắn nhất từ một điểm sử dụng Min-Heap"""
    dist = {node: float("inf") for node in graph}
    parent = {node: None for node in graph}

    if source not in graph:
        return dist, parent

    dist[source] = 0
    min_heap = [(0, source)]

    while min_heap:
        current_dist, u = heapq.heappop(min_heap)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            distance = current_dist + weight
            if distance < dist[v]:
                dist[v] = distance
                parent[v] = u
                heapq.heappush(min_heap, (distance, v))

    return dist, parent


def shortest_route(graph, source, target):
    """Trả về chi phí và danh sách các trạm đi qua"""
    if source not in graph or target not in graph:
        return float("inf"), []

    dist, parent = dijkstra(graph, source)
    if dist[target] == float("inf"):
        return float("inf"), []

    route = []
    curr = target
    while curr is not None:
        route.append(curr)
        curr = parent[curr]
    route.reverse()

    return dist[target], route


def demo_routing_shortest_path():
    print("\n--- DEMO 1.1: TÌM TUYẾN GIAO HÀNG NGẮN NHẤT (DIJKSTRA) ---")
    edges = [
        ("WH1", "WH2", 13),
        ("WH1", "HN", 13),
        ("HN", "DN", 15),
        ("WH2", "DN", 23),
        ("WH2", "HCM", 22),
        ("DN", "HCM", 8),
        ("DN", "WH3", 12),
        ("HCM", "WH3", 4),
    ]
    graph = build_graph(edges)
    source, target = "WH1", "HCM"
    cost, route = shortest_route(graph, source, target)

    print(f"Điểm xuất phát: {source} -> Điểm đích: {target}")
    print(f"Tuyến đường tối ưu: {' -> '.join(route)}")
    print(f"Tổng chi phí vận chuyển (Thời gian/Quãng đường): {cost}")


class DSU:
    """Cấu trúc dữ liệu các tập hợp rời nhau tối ưu với Path Compression & Union by Size"""

    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.size = {v: 1 for v in vertices}

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True
        return False


def kruskal_mst(vertices, edges):
    """Tìm cây khung nhỏ nhất liên kết các kho trục chính"""
    dsu = DSU(vertices)
    sorted_edges = sorted(edges, key=lambda item: item[2])
    mst = []
    total_cost = 0

    for u, v, cost in sorted_edges:
        if dsu.union(u, v):
            mst.append((u, v, cost))
            total_cost += cost
            if len(mst) == len(vertices) - 1:
                break
    return mst, total_cost


def demo_mst_network():
    print("\n--- DEMO 1.2: THIẾT KẾ MẠNG LIÊN KẾT KHO TỐI THIỂU (MST) ---")
    vertices = ["WH1", "WH2", "HN", "DN", "HCM", "WH3"]
    edges = [
        ("WH1", "WH2", 10),
        ("WH1", "HN", 5),
        ("HN", "DN", 15),
        ("WH2", "DN", 7),
        ("WH2", "HCM", 20),
        ("DN", "HCM", 8),
        ("DN", "WH3", 12),
        ("HCM", "WH3", 4),
    ]
    mst, total_cost = kruskal_mst(vertices, edges)

    print("Các tuyến trục chính liên kho được lựa chọn lắp đặt đường truyền:")
    for u, v, cost in mst:
        print(f"  - Cổng kết nối {u} <---> {v} (Chi phí: {cost})")
    print(f"-> Tổng chi phí lắp đặt liên kết tối thiểu: {total_cost}")
    print(
        "\n> NHẬN XÉT: Đây là bộ khung tối thiểu đảm bảo toàn bộ hệ thống kho liên thông."
    )
    print(
        "  Các tuyến giao nhận chi tiết phát sinh hàng ngày sẽ chạy Dijkstra trên mạng lưới này."
    )


class OrderHashTable:
    def __init__(self, capacity=1007):
        self.capacity = capacity
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, order_id, order_data):
        index = self._hash(order_id)
        for item in self.table[index]:
            if item[0] == order_id:
                item[1] = order_data
                return
        self.table[index].append([order_id, order_data])

    def get(self, order_id):
        index = self._hash(order_id)
        for item in self.table[index]:
            if item[0] == order_id:
                return item[1]
        return None

    def remove(self, order_id):
        index = self._hash(order_id)
        for i, item in enumerate(self.table[index]):
            if item[0] == order_id:
                del self.table[index][i]
                return True
        return False


def demo_order_hash_table():
    print("\n--- DEMO 2.1: TRA CỨU ĐƠN HÀNG VỚI HASH TABLE ---")
    ht = OrderHashTable()
    ht.insert("ORD001", {"Customer": "An", "Status": "Processing", "Total": 250000})
    ht.insert("ORD002", {"Customer": "Bình", "Status": "Shipped", "Total": 540000})

    print("1. Thêm thành công ORD001, ORD002 vào Hash Table.")
    print(f"2. Truy vấn nhanh ORD001: {ht.get('ORD001')}")
    ht.remove("ORD001")
    print("3. Xóa đơn hàng ORD001 khỏi hệ thống.")
    print(f"4. Thử truy vấn lại ORD001: {ht.get('ORD001')} (Không tìm thấy)")


def group_coupon_anagrams(codes):
    ans = {}
    for code in codes:
        count_key = "".join(sorted(code))
        if count_key not in ans:
            ans[count_key] = []
        ans[count_key].append(code)
    return list(ans.values())


def demo_group_anagrams():
    print("\n--- DEMO 2.2: NHÓM MÃ COUPON ĐỒNG CẤU TRÚC (ANAGRAMS) ---")
    coupons = ["SAVE10", "AVES10", "EVAS10", "DISCOUNT", "COUNIDST", "POLYSHIP"]
    grouped = group_coupon_anagrams(coupons)
    print(f"Danh sách gốc: {coupons}")
    print("Kết quả nhóm:")
    for idx, group in enumerate(grouped):
        print(f"  Nhóm {idx + 1}: {group}")
    print(
        "> Ứng dụng: Giúp hệ thống phát hiện các mã 'na ná nhau', chống gian lận/trùng lặp."
    )


def longest_consecutive_days(days):
    day_set = set(days)
    longest_streak = 0
    for day in day_set:
        if day - 1 not in day_set:
            current_day = day
            current_streak = 1
            while current_day + 1 in day_set:
                current_day += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak


def demo_longest_consecutive():
    print("\n--- DEMO 2.3: CHUỖI NGÀY HOẠT ĐỘNG CAO ĐIỂM LIÊN TIẾP ---")
    days = [100, 4, 200, 1, 3, 2, 101, 102, 5]
    streak = longest_consecutive_days(days)
    print(f"Các ngày hệ thống ghi nhận sự kiện/đơn hàng: {days}")
    print(f"-> Chuỗi ngày liên tục dài nhất: {streak} ngày (từ ngày 1 đến ngày 5)")


def count_revenue_windows(revenues, k):
    count = 0
    curr_sum = 0
    prefix_sums = {0: 1}
    for rev in revenues:
        curr_sum += rev
        if curr_sum - k in prefix_sums:
            count += prefix_sums[curr_sum - k]
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
    return count


def demo_subarray_sum():
    print("\n--- DEMO 2.4: ĐẾM KHOẢNG NGÀY ĐẠT ĐÚNG MỤC TIÊU DOANH THU ---")
    revenues = [10, 2, -2, -20, 10]
    target = -10
    windows = count_revenue_windows(revenues, target)
    print(f"Chuỗi doanh thu hàng ngày: {revenues}")
    print(f"Doanh thu mục tiêu cần tìm (k) = {target}")
    print(f"-> Số khoảng ngày liên tiếp đạt tổng doanh thu trên: {windows}")


def rolling_hash_search(text, pattern):
    d = 256
    q = 101
    d = 256
    q = 101
    M = len(pattern)
    N = len(text)
    p = 0
    t = 0
    p = 0
    t = 0
    h = 1
    results = []

    if M > N or M == 0:
        return results

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(N - M + 1):
        if p == t:
            if text[i : i + M] == pattern:
                results.append(i)
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t = t + q
    return results


def demo_rolling_coupon_search():
    print("\n--- DEMO 2.5: TÌM MÃ KHUYẾN MÃI TRONG LOG HỆ THỐNG (ROLLING HASH) ---")
    log_text = "LOG_USER_123_APPLIED_SUMMER20_AT_TIMESTAMP_POLYSHIP_SUMMER20_SUCCESS"
    pattern = "SUMMER20"
    matches = rolling_hash_search(log_text, pattern)
    print(f"Nội dung Log chuỗi: '{log_text}'")
    print(f"Mã cần định vị: '{pattern}'")
    print(f"-> Tìm thấy mã xuất hiện tại các vị trí Index: {matches}")


def fib_tab(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def climb_stairs(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def demo_dp_basics():
    print("\n--- DEMO 3.1: ĐỘNG LỰC HỌC QUY HOẠCH ĐỘNG CƠ BẢN ---")
    n = 6
    print(f"Fibonacci số thứ {n} = {fib_tab(n)}")
    print(
        f"Số cách để shipper leo {n} bậc thang (mỗi bước 1 hoặc 2 bậc): {climb_stairs(n)}"
    )


def build_combo_dp_table(prices, scores, B):
    n = len(prices)
    dp = [[0] * (B + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for b in range(B + 1):
            if prices[i - 1] <= b:
                dp[i][b] = max(
                    scores[i - 1] + dp[i - 1][b - prices[i - 1]], dp[i - 1][b]
                )
            else:
                dp[i][b] = dp[i - 1][b]
    return dp


def trace_combo_from_dp(dp, prices, scores, B):
    selected_indices = []
    i = len(prices)
    b = B
    while i > 0 and b > 0:
        if dp[i][b] != dp[i - 1][b]:
            selected_indices.append(i - 1)
            b -= prices[i - 1]
        i -= 1
    selected_indices.reverse()
    return selected_indices


def demo_combo_knapsack_2d():
    print("\n--- DEMO 3.2: TỐI ƯU GÓI COMBO SẢN PHẨM KHUYẾN MÃI (DP 2D) ---")
    products = [
        "Chuột máy tính",
        "Bàn phím cơ",
        "Tai nghe Gaming",
        "Lót chuột cỡ lớn",
        "Webcam HD",
    ]
    prices = [200, 300, 400, 100, 350]
    scores = [40, 65, 70, 25, 60]
    budget = 600
    prices = [200, 300, 400, 100, 350]
    scores = [40, 65, 70, 25, 60]
    budget = 600

    dp_table = build_combo_dp_table(prices, scores, budget)
    max_score = dp_table[len(prices)][budget]
    selected_idx = trace_combo_from_dp(dp_table, prices, scores, budget)

    print(f"Ngân sách tối đa của gói Combo: {budget}k")
    print("Danh sách sản phẩm hệ thống đang có (Giá, Điểm đánh giá):")
    for i in range(len(products)):
        print(f"  - {products[i]}: ({prices[i]}k, Score: {scores[i]})")

    print(f"\n-> Điểm thưởng tối ưu đạt được: {max_score}")
    print("Các sản phẩm tối ưu nhất được gom vào gói Combo:")
    for idx in selected_idx:
        print(f"  [+] {products[idx]} (Giá: {prices[idx]}k)")


def combo_knapsack_1d(prices, scores, B):
    dp = [0] * (B + 1)
    for i in range(len(prices)):
        for b in range(B, prices[i] - 1, -1):
            dp[b] = max(dp[b], scores[i] + dp[b - prices[i]])
    return dp[B]


def demo_combo_knapsack_1d():
    print("\n--- DEMO 3.3: TỐI ƯU KHÔNG GIAN BỘ NHỚ VỚI DP MẢNG 1 CHIỀU ---")
    prices = [200, 300, 400, 100, 350]
    scores = [40, 65, 70, 25, 60]
    budget = 600

    max_score_1d = combo_knapsack_1d(prices, scores, budget)
    print(f"Tổng điểm thưởng tối đa giải bằng mảng 1D: {max_score_1d}")
    print(
        "> Nhận xét: Kết quả 1D trùng khớp hoàn toàn với bảng 2D nhưng tối ưu tài nguyên phần cứng cực tốt."
    )


def display_menu():
    print("\n" + "=" * 60)
    print("       HỆ THỐNG GIẢI THUẬT HẬU CẦN CORE - POLY-SHIP")
    print("=" * 60)
    print("1. Demo Routing - Tuyến giao hàng ngắn nhất (Dijkstra)")
    print("2. Demo MST - Thiết kế trục kết nối mạng kho (Kruskal)")
    print("3. Demo Hash Table - Tra cứu quản lý mã đơn hàng")
    print("4. Demo Hashing mở rộng - Nhóm Anagram, Ngày liên tiếp, Tổng k")
    print("5. Demo Rolling Hash - Khớp mẫu chuỗi tìm Coupon trong Log")
    print("6. Demo Quy hoạch động cơ bản - Stairs & Fibonacci")
    print("7. Demo Thiết kế Combo Khuyến mãi - Knapsack 0/1 (2D & 1D)")
    print("8. Thoát chương trình")
    print("=" * 60)


def main():
    while True:
        display_menu()
        try:
            choice = int(input("Nhập số tính năng muốn chạy thử (1-8): "))
        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng số nguyên!")
            continue

        if choice == 1:
            demo_routing_shortest_path()
        elif choice == 2:
            demo_mst_network()
        elif choice == 3:
            demo_order_hash_table()
        elif choice == 4:
            demo_group_anagrams()
            demo_longest_consecutive()
            demo_subarray_sum()
        elif choice == 5:
            demo_rolling_coupon_search()
        elif choice == 6:
            demo_dp_basics()
        elif choice == 7:
            demo_combo_knapsack_2d()
            demo_combo_knapsack_1d()
        elif choice == 8:
            print("\nHệ thống POLY-SHIP dừng chạy thử. Chúc bạn một ngày tốt lành!")
            sys.exit()
        else:
            print("Mục chọn không hợp lệ, vui lòng thử lại từ 1 đến 8.")


if __name__ == "__main__":
    main()
