
def permutations(nums):
    """Tìm tất cả hoán vị của nums"""
    result = []
    
    def backtrack(path, remaining):
        if len(path) == len(nums):
            result.append(path.copy()) 
            return
            
        for i in range(len(remaining)):
            path.append(remaining[i])
            
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(path, new_remaining)
            
            path.pop()
            
    backtrack([], nums)
    return result

def combinations(nums, k):
    """Tìm tất cả tổ hợp k phần tử từ nums"""
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path.copy())
            return
            
        for i in range(start, len(nums)):
            path.append(nums[i])
            
            backtrack(i + 1, path)
            
            path.pop()
            
    backtrack(0, [])
    return result


def subsets(nums):
    """Tìm tất cả tập con của nums"""
    result = []
    
    def backtrack(start, path):
        result.append(path.copy())
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            
            backtrack(i + 1, path)
            
            path.pop()
            
    backtrack(0, [])
    return result


def binary_strings(n):
    """Tìm tất cả chuỗi nhị phân độ dài n"""
    result = []
    
    def backtrack(path):
        if len(path) == n:
            result.append(''.join(path))
            return
            
        for choice in ['0', '1']:
            path.append(choice)
            
            backtrack(path)
            
            path.pop()
            
    backtrack([])
    return result


if __name__ == "__main__":
    print("=== Test Permutations ===")
    res_p1 = permutations([1, 2, 3])
    print(f"Hoán vị của [1,2,3]: {res_p1}\nSố lượng: {len(res_p1)}")
    res_p2 = permutations([1, 2])
    print(f"Hoán vị của [1,2]: {res_p2}\nSố lượng: {len(res_p2)}")
    
    print("\n=== Test Combinations ===")
    res_c1 = combinations([1, 2, 3, 4], 2)
    print(f"Tổ hợp 2 từ [1,2,3,4]: {res_c1}\nSố lượng: {len(res_c1)}")
    res_c2 = combinations([1, 2, 3], 2)
    print(f"Tổ hợp 2 từ [1,2,3]: {res_c2}\nSố lượng: {len(res_c2)}")
    
    print("\n=== Test Subsets ===")
    res_s1 = subsets([1, 2, 3])
    print(f"Tập con của [1,2,3]: {res_s1}\nSố lượng: {len(res_s1)}")
    res_s2 = subsets([1, 2])
    print(f"Tập con của [1,2]: {res_s2}\nSố lượng: {len(res_s2)}")
    
    print("\n=== Test Binary Strings ===")
    res_b1 = binary_strings(3)
    print(f"Chuỗi nhị phân độ dài 3: {res_b1}\nSố lượng: {len(res_b1)}")
    res_b2 = binary_strings(2)
    print(f"Chuỗi nhị phân độ dài 2: {res_b2}\nSố lượng: {len(res_b2)}")