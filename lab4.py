
def activity_selection(activities):
    """
    Chọn số lượng hoạt động tối đa không chồng lấp.
    Chiến lược Greedy: Luôn chọn hoạt động có thời gian kết thúc sớm nhất 
    (Earliest Finish Time) để dành nhiều khoảng trống thời gian cho các hoạt động sau.
    
    Input: activities = [(start, finish), ...]
    Output: list của các hoạt động được chọn
    """
    if not activities:
        return []
    
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_finish = activities[0][1]
    
    for i in range(1, len(activities)):
        start, finish = activities[i]
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
            
    return selected


def coin_change_greedy(amount, coins):
    """
    Đổi tiền bằng số xu ít nhất theo thuật toán Tham lam.
    Chiến lược Greedy: Luôn chọn mệnh giá lớn nhất có thể tại mỗi bước 
    để giảm số tiền cần đổi nhanh nhất.
    
    LƯU Ý: Chỉ đúng với hệ tiền chuẩn (canonical coin system)!
    Input: amount (số tiền), coins (list mệnh giá)
    Output: (số xu ít nhất, list các xu đã dùng) hoặc (-1, []) nếu không đổi được
    """
    coins.sort(reverse=True)
    
    count = 0 
    result = [] 
    

    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin
            count += 1
            
    if amount == 0:
        return count, result
    else:
        return -1, []


def fractional_knapsack(capacity, items):
    """
    Bài toán Ba lô phân số (Fractional Knapsack).
    Chiến lược Greedy: Tính tỷ lệ giá trị trên trọng lượng (value/weight) của từng vật.
    Ưu tiên lấy toàn bộ hoặc một phần vật có tỷ lệ này cao nhất trước.
    
    Input: capacity (sức chứa), items = [(weight, value), ...]
    Output: (giá trị tối đa, list chi tiết chọn vật [(w, v, fraction)])
    """
    items_with_ratio = []
    for weight, value in items:
        ratio = value / weight
        items_with_ratio.append((weight, value, ratio))
        
    items_with_ratio.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    result = []
    
    for weight, value, ratio in items_with_ratio:
        if remaining_capacity == 0:
            break
            
        if weight <= remaining_capacity: 
            total_value += value
            remaining_capacity -= weight
            result.append((weight, value, 1.0))
        else:
            fraction = remaining_capacity / weight
            total_value += value * fraction
            result.append((weight, value, fraction))
            remaining_capacity = 0 
            
    return total_value, result


def min_intervals_remove(intervals):
    """
    Tìm số khoảng thời gian ít nhất cần xóa để các khoảng còn lại không chồng lấp.
    Chiến lược Greedy: Biến đổi bài toán thành tìm số lượng các khoảng tối đa giữ lại 
    (chính là bài toán Activity Selection). 
    Số lượng cần xóa = Tổng số khoảng ban đầu - Số khoảng tối đa giữ lại được.
    """
    if not intervals:
        return 0
        
    intervals_copy = list(intervals)
    max_keep = activity_selection(intervals_copy)
    
    num_remove = len(intervals) - len(max_keep)
    return num_remove


if __name__ == "__main__":
    print("=== Test Activity Selection ===")
    activities1 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    res1 = activity_selection(activities1)
    print(f"Hoạt động được chọn: {res1}\nSố lượng: {len(res1)} (Kỳ vọng: 4)")
    
    activities2 = [(1, 3), (2, 4), (3, 5), (4, 6)]
    res2 = activity_selection(activities2)
    print(f"Hoạt động được chọn: {res2}\nSố lượng: {len(res2)} (Kỳ vọng: 2)")

    print("\n=== Test Coin Change Greedy ===")
    print("Test 1: Hệ tiền chuẩn USD [25, 10, 5, 1]")
    c1, r1 = coin_change_greedy(63, [25, 10, 5, 1])
    print(f"Số xu: {c1} | Chi tiết: {r1} (Kỳ vọng: 6 xu [25, 25, 10, 1, 1, 1])")
    
    print("\nTest 2: Hệ tiền VN [500, 200, 100, 50, 20, 10]")
    c2, r2 = coin_change_greedy(370, [500, 200, 100, 50, 20, 10])
    print(f"Số xu: {c2} | Chi tiết: {r2} (Kỳ vọng: 4 xu [200, 100, 50, 20])")
    
    print("\nTest 3: Hệ mệnh giá lạ [25, 10, 1] (Greedy SAI!)")
    c3, r3 = coin_change_greedy(30, [25, 10, 1])
    print(f"Số xu Greedy: {c3} | Chi tiết: {r3}")
    print("⚠️ CHÚ Ý: Greedy cho 6 xu nhưng tối ưu thực tế là 3 xu [10, 10, 10]!")

    print("\n=== Test Fractional Knapsack ===")
    cap1 = 50
    items1 = [(10, 60), (20, 100), (30, 120)]
    v1, det1 = fractional_knapsack(cap1, items1)
    print(f"Sức chứa: {cap1} | Giá trị tối đa: {v1}")
    for w, v, f in det1: print(f" - Vật (w={w}, v={v}): Lấy {f*100:.1f}%")

    print("\n=== Test Minimum Intervals Remove ===")
    int1 = [(1, 2), (2, 3), (3, 4), (1, 3)]
    print(f"Intervals: {int1} -> Số khoảng cần xóa: {min_intervals_remove(int1)} (Kỳ vọng: 1)")
    int2 = [(1, 2), (1, 2), (1, 2)]
    print(f"Intervals: {int2} -> Số khoảng cần xóa: {min_intervals_remove(int2)} (Kỳ vọng: 2)")
    int3 = [(1, 100), (11, 22), (1, 11), (2, 12)]
    print(f"Intervals: {int3} -> Số khoảng cần xóa: {min_intervals_remove(int3)} (Kỳ vọng: 2)")