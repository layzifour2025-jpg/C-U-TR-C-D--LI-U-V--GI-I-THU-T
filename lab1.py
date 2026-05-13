import time
import random

# BÀI 1: PHÂN TÍCH ĐỘ PHỨC TẠP CƠ BẢN

def snippet_1(n):
    total = 0 
    for i in range(n): 
        total = total + 1
    return total
# Độ phức tạp: O(n)
# Giải thích: Vòng for chạy n lần, mỗi lần thực hiện phép cộng hằng số.

def snippet_2(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count
# Độ phức tạp: O(n^2)
# Giải thích: Có 2 vòng for lồng nhau, mỗi vòng chạy n lần -> n * n = n^2 bước.

def snippet_3(n):
    steps = 0
    while n > 0:
        n = n // 2
        steps += 1
    return steps
# Độ phức tạp: O(log n)
# Giải thích: Mỗi bước n bị chia đôi, số lần lặp tương ứng với số lần chia đôi n về 1.

def constant_work():
    return 1 + 2

def snippet_4(n):
    for i in range(n):
        constant_work()
# Độ phức tạp: O(n)
# Giải thích: Vòng for chạy n lần, mỗi lần gọi hàm có độ phức tạp O(1).

# BÀI 2: PHÂN TÍCH VÒNG LẶP BIẾN THỂ VÀ TỐI ƯU

def snippet_5(n):
    total = 0
    for i in range(n):
        for j in range(i):
            total += 1
    return total
# Độ phức tạp: O(n^2)
# Giải thích: Tổng số lần lặp là 0+1+2...+(n-1) = n(n-1)/2, vẫn thuộc bậc n^2.

def snippet_6(n):
    k = 1
    total = 0
    while k < n:
        for i in range(n):
            total += 1
        k = k * 2
    return total
# Độ phức tạp: O(n log n)
# Giải thích: Vòng while chạy log(n) lần, mỗi lần chạy vòng for n lần.

def snippet_7(arr):
    count = 0
    for x in arr:
        if x in arr: 
            count += 1
    return count
# Độ phức tạp: O(n^2)
# Giải thích: Vòng for chạy n lần, toán tử 'in' trên list tốn O(n).

def snippet_8(arr):
    s = set(arr)
    count = 0
    for x in arr:
        if x in s:
            count += 1
    return count
# Độ phức tạp: O(n)
# Giải thích: Tạo set tốn O(n), vòng for chạy n lần với toán tử 'in' trên set chỉ tốn O(1).

# BÀI 3: TỐI ƯU THUẬT TOÁN (TWO SUM)

def two_sum_quadratic(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None
# Độ phức tạp: O(n^2)
# Giải thích: Sử dụng 2 vòng lặp lồng nhau để kiểm tra mọi cặp chỉ số.

def two_sum_linear(arr, target):
    seen = {} # key: giá trị, value: chỉ số
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in seen:
            return (seen[complement], i)
        seen[arr[i]] = i
    return None
# Độ phức tạp: O(n)
# Giải thích: Chỉ duyệt mảng 1 lần, sử dụng dictionary để tìm kiếm giá trị bù trong O(1).

# ĐO THỜI GIAN VÀ SO SÁNH
if __name__ == "__main__":
    # Test với dữ liệu lớn cho O(n)
    n_large = 100000
    arr_large = list(range(n_large))
    random.shuffle(arr_large)
    target = arr_large[100] + arr_large[999]

    print(f"--- So sánh với n = {n_large} ---")
    start = time.perf_counter()
    two_sum_linear(arr_large, target)
    print(f"Thời gian O(n): {time.perf_counter() - start:.6f} giây")

    # Test với dữ liệu nhỏ cho O(n^2) vì O(n^2) rất chậm
    n_small = 5000
    arr_small = list(range(n_small))
    random.shuffle(arr_small)
    target_small = arr_small[10] + arr_small[4000]

    print(f"\n--- So sánh với n = {n_small} ---")
    start = time.perf_counter()
    two_sum_quadratic(arr_small, target_small)
    print(f"Thời gian O(n^2): {time.perf_counter() - start:.6f} giây")
