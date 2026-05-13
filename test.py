# import time
# def has_duplicates_v1(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]==arr[j]:
#                 return True
#     return False

# def has_duflicate(arr):
#     seen=set()
#     for item in arr:
#         if item in seen:
#             return True
#         seen.add(item)
#     return False

# arr=list(range(10000))
# arr.append(5000)
# start = time.time()
# result1=has_duflicate(arr)
# time1 = time.time() - start
# print(f"Cách 1: {time1:.4f} giây")

# start = time.time()
# result2=has_duplicates_v1(arr)
# time2 = time.time() - start
# print(f"Cách 2: {time2:.4f} giây")
def two_sum_v1(nums, target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []
def two_sum_v2(nums, target):
    seen={}
    for i, num in enumerate(nums):
        complement=target-num
        if complement in seen:
            return [seen[complement],i]
        seen[num]=i
    return []
