# # import time
# # def has_duplicates_v1(arr):
# #     n=len(arr)
# #     for i in range(n):
# #         for j in range(i+1,n):
# #             if arr[i]==arr[j]:
# #                 return True
# #     return False

# # def has_duflicate(arr):
# #     seen=set()
# #     for item in arr:
# #         if item in seen:
# #             return True
# #         seen.add(item)
# #     return False

# # arr=list(range(10000))
# # arr.append(5000)
# # start = time.time()
# # result1=has_duflicate(arr)
# # time1 = time.time() - start
# # print(f"Cách 1: {time1:.4f} giây")

# # start = time.time()
# # result2=has_duplicates_v1(arr)
# # time2 = time.time() - start
# # # print(f"Cách 2: {time2:.4f} giây")
# # def two_sum_v1(nums, target):
# #     n=len(nums)
# #     for i in range(n):
# #         for j in range(i+1,n):
# #             if nums[i]+nums[j]==target:
# #                 return [i,j]
# #     return []
# # def two_sum_v2(nums, target):
# #     seen={}
# #     for i, num in enumerate(nums):
# #         complement=target-num
# #         if complement in seen:
# #             return [seen[complement],i]
# #         seen[num]=i
# #     return []



# # def factorial(n):
# #     if n == 0 or n == 1:
# #         return 1
# #     else:
# #         return n * factorial(n - 1)
    
# # def sum_to_n(n):
# #     if n == 1:
# #         return 1
# #     return n + sum_to_n(n - 1)    
# # ------------------------------------------------------------------------
# # from matplotlib.pylab import partition


# # def merge_sort(arr):
# #     if len(arr) <= 1:
# #         return arr
# #     mid = len(arr) // 2
# #     left_half = merge_sort(arr[:mid])
# #     right_half = merge_sort(arr[mid:])
# #     return merge(left_half, right_half)

# # def merge(left, right):
# #     result = []
# #     i = j = 0
# #     while i < len(left) and j < len(right):
# #         if left[i] < right[j]:
# #             result.append(left[i])
# #             i += 1
# #         else:
# #             result.append(right[j])
# #             j += 1
# #     result.extend(left[i:])
# #     result.extend(right[j:])
# #     return result
# # arr = [38, 27, 43, 3, 9, 82, 10, ]
# # sorted_arr = merge_sort(arr)
# # print(sorted_arr)

# # def quick_sort(arr, low, high):
# #     if low < high:
# #         pi = partition(arr, low, high)
# #         quick_sort(arr, low, pi - 1)
# #         quick_sort(arr, pi + 1, high)

# # def partition(arr, low, high):
# #     i = low - 1
# #     pivot = arr[high]
# #     for j in range(low, high):
# #         if arr[j] < pivot:
# #             i += 1
# #             arr[i], arr[j] = arr[j], arr[i]
# #     arr[i + 1], arr[high] = arr[high], arr[i + 1]
# #     return i + 1

# # arr = [38, 27, 43, 3, 9, 82, 10]
# # quick_sort(arr, 0, len(arr) - 1)    
# # print("mang ban dau: ", arr )
# # print("mang sau khi sap xep: ", arr)
# def activity_selection(activities):
#     """activities: list of tuples (start, finish)
#     return: list of selected activities"""
#     activities.sort(key=lambda x: x[1])
#     selected = [activities[0]]
#     last_finish = activities[0][1]
#     for i in range(1, len(activities)):
#         if activities[i][0] >= last_finish:
#             selected.append(activities[i])
#             last_finish = activities[i][1]
#     return selected

# activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11)]
# result = activity_selection(activities)
# print(result)+
def has_cycle_directed(graph):
    # Bước 1: Khởi tạo tất cả các đỉnh với màu WHITE (Chưa thăm)
    color = {}
    for vertex in graph:
        color[vertex] = 'WHITE'

    # Bước 3: Định nghĩa hàm đệ quy DFS
    def dfs(vertex):
        # a. Đánh dấu đỉnh hiện tại là GRAY (Đang thăm)
        color[vertex] = 'GRAY'
        
        # b. Duyệt qua từng đỉnh kề (neighbor) của đỉnh hiện tại
        # Dùng graph.get(vertex, []) để tránh lỗi nếu đỉnh không có đỉnh kề nào
        for neighbor in graph.get(vertex, []):
            
            # Nếu đỉnh kề đang màu GRAY -> Đã quay lại đường cũ -> CÓ CHU TRÌNH
            if color.get(neighbor) == 'GRAY':
                return True
                
            # Nếu đỉnh kề màu WHITE -> Chưa thăm -> Tiếp tục đi sâu (đệ quy)
            elif color.get(neighbor) == 'WHITE':
                # Nếu nhánh đệ quy này tìm thấy chu trình, báo True ngay lập tức
                if dfs(neighbor):
                    return True
                    
        # c. Sau khi duyệt xong tất cả các kề mà không có chu trình
        # Đánh dấu đỉnh là BLACK (Đã thăm xong toàn bộ nhánh)
        color[vertex] = 'BLACK'
        
        # d. Nhánh này an toàn, không có chu trình
        return False

    # Bước 2: Duyệt qua từng đỉnh của đồ thị để đảm bảo không bỏ sót đồ thị không liên thông
    for vertex in graph:
        if color[vertex] == 'WHITE':
            # Chạy DFS từ đỉnh này, nếu phát hiện chu trình thì dừng và báo True
            if dfs(vertex):
                return True

    # Bước 4: Duyệt hết tất cả các đỉnh mà không thấy chu trình
    return False


# ==========================================
# VÍ DỤ CHẠY THỬ (TEST CASES)
# ==========================================

if __name__ == "__main__":
    # Đồ thị 1: KHÔNG có chu trình (A -> B -> C, A -> C)
    graph_no_cycle = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': []
    }
    
    # Đồ thị 2: CÓ chu trình (A -> B -> C -> A)
    graph_with_cycle = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A'] 
    }

    print("Kiểm tra đồ thị 1 (Không chu trình):", has_cycle_directed(graph_no_cycle)) 
    # Kết quả mong đợi: False

    print("Kiểm tra đồ thị 2 (Có chu trình):", has_cycle_directed(graph_with_cycle)) 
    # Kết quả mong đợi: True

    def