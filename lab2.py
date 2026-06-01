import time
import random
import sys

sys.setrecursionlimit(20000)


# BÀI 1 – VIẾT HÀM ĐỆ QUY CƠ BẢN

print("=" * 60)
print("BÀI 1: CÁC HÀM ĐỆ QUY CƠ BẢN")
print("=" * 60)

# --- Hàm 1 – Tính tổng từ 1 đến n ---
def sum_to_n(n):
    """
    Tính tổng 1 + 2 + ... + n bằng đệ quy
    
    - Base case: n = 0 trả về 0, n = 1 trả về 1. Đây là điểm dừng cố định.
    - Recursive case: n + sum_to_n(n - 1). Gọi lại chính nó với bài toán nhỏ hơn (n-1).
    - Độ phức tạp thời gian (Time Complexity): O(n) - Hàm gọi đệ quy n lần.
    - Độ phức tạp không gian (Space Complexity): O(n) - Bộ nhớ lưu trữ n stack frame.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)

print("--- Test Hàm 1: sum_to_n ---")
print(f"sum_to_n(5)   = {sum_to_n(5)}")     
print(f"sum_to_n(100) = {sum_to_n(100)}")   


# --- Hàm 2 – Tính n mũ k (power) ---
def power(n, k):
    """
    Tính n^k bằng đệ quy
    
    - Base case: Số mũ k = 0 trả về 1. Cơ số n = 0 trả về 0.
    - Recursive case: n * power(n, k - 1). Nhân cơ số với luỹ thừa mũ giảm dần.
    - Độ phức tạp thời gian (Time Complexity): O(k) - Hàm lặp đệ quy k lần theo số mũ.
    - Độ phức tạp không gian (Space Complexity): O(k) - Độ sâu stack đệ quy là k.
    """
    if k == 0:
        return 1
    if n == 0:
        return 0
    return n * power(n, k - 1)

print("\n--- Test Hàm 2: power ---")
print(f"power(2, 5) = {power(2, 5)}")       
print(f"power(3, 4) = {power(3, 4)}")     


# --- Hàm 3 – Đảo chuỗi (reverse string) ---
def reverse_string(s):
    """
    Đảo ngược chuỗi bằng đệ quy
    
    - Base case: Chuỗi rỗng hoặc có 1 ký tự (len(s) <= 1) thì giữ nguyên và trả về chính nó.
    - Recursive case: reverse_string(s[1:]) + s[0]. Đảo ngược phần đuôi rồi ghép ký tự đầu xuống cuối.
    - Độ phức tạp thời gian (Time Complexity): O(n) - Với n là chiều dài chuỗi.
    - Độ phức tạp không gian (Space Complexity): O(n) - Tốn bộ nhớ để cắt chuỗi và lưu call stack.
    """
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print("\n--- Test Hàm 3: reverse_string ---")
print(f"reverse_string('hello')  = '{reverse_string('hello')}'")   
print(f"reverse_string('python') = '{reverse_string('python')}'") 


def is_palindrome(s):
    """
    Kiểm tra chuỗi đối xứng (palindrome) bằng đệ quy
    
    - Base case: Chuỗi rỗng hoặc chỉ có 1 ký tự (len(s) <= 1) luôn đối xứng -> True.
    - Recursive case: Nếu s[0] == s[-1] (ký tự đầu bằng cuối), tiếp tục đệ quy phần ở giữa s[1:-1].
                      Ngược lại nếu khác nhau lập tức trả về False.
    - Độ phức tạp thời gian (Time Complexity): O(n) - Thực hiện tối đa n/2 lần so sánh.
    - Độ phức tạp không gian (Space Complexity): O(n) - Do tạo chuỗi con và lưu call stack.
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print("\n--- Test Hàm 4: is_palindrome ---")
print(f"is_palindrome('racecar') = {is_palindrome('racecar')}")   # True
print(f"is_palindrome('python')  = {is_palindrome('python')}")    # False



print("\n" + "=" * 60)
print("BÀI 2: TỐI ƯU FIBONACCI VỚI MEMOIZATION & VÒNG LẶP")
print("=" * 60)

def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return memo[n]
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

def fibonacci_iterative(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

print("--- So sánh hiệu suất tính Fibonacci ---")
start = time.time()
res_naive = fibonacci_naive(30) 
time_naive = time.time() - start
print(f"Naive F(30)       = {res_naive}, Thời gian: {time_naive:.4f}s")

start = time.time()
res_memo = fibonacci_memo(100) 
time_memo = time.time() - start
print(f"Memoization F(100) = {res_memo}, Thời gian: {time_memo:.6f}s")

start = time.time()
res_iter = fibonacci_iterative(100)
time_iter = time.time() - start
print(f"Iterative F(100)   = {res_iter}, Thời gian: {time_iter:.6f}s")


print("\n" + "=" * 60)
print("BÀI 3: THUẬT TOÁN SẮP XẾP CHIA ĐỂ TRỊ")
print("=" * 60)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print("--- Kiểm tra chức năng sắp xếp cơ bản ---")
arr_test = [64, 34, 25, 12, 22, 11, 90]
print(f"Mảng gốc:        {arr_test}")
print(f"Merge Sort xong: {merge_sort(arr_test.copy())}")
print(f"Quick Sort xong: {quick_sort(arr_test.copy())}")

print("\n--- Đo thời gian thực thi với mảng kích thước lớn ---")
arr_small = [random.randint(1, 1000) for _ in range(100)]
arr_large = [random.randint(1, 10000) for _ in range(5000)]

start = time.time()
_ = merge_sort(arr_small.copy())
print(f"[Merge Sort] Thắng mảng nhỏ  (100 pử): {time.time() - start:.6f}s")

start = time.time()
_ = merge_sort(arr_large.copy())
print(f"[Merge Sort] Thắng mảng lớn (5000 pử): {time.time() - start:.6f}s")

start = time.time()
_ = quick_sort(arr_large.copy())
print(f"[Quick Sort] Thắng mảng lớn (5000 pử): {time.time() - start:.6f}s")

start = time.time()
_ = sorted(arr_large)
print(f"[Built-in]   Thời gian Python sorted():       {time.time() - start:.6f}s")