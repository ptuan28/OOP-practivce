"""Two Sum — hash map O(n)
Cho mảng N số nguyên và target T. 
Tìm cặp chỉ số i < j sao cho a[i] + a[j] == T.
In i j (0-indexed).
Đề đảm bảo có đúng 1 cặp."""

"""Format input / output
Input: dòng 1 N T, dòng 2 là N số
Output: 2 chỉ số i j (i < j)"""

# n, t = map(int, input().split())
# a = list(map(int, input().split()))
# # TODO: dict{value -> index}; với mỗi j, check t - a[j] đã thấy chưa
# # In i, j cách nhau space

import sys

def solve():
    # Đọc dữ liệu từ stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # n là số lượng phần tử, t là target
    n = int(input_data[0])
    t = int(input_data[1])
    
    # a là danh sách các số
    a = list(map(int, input_data[2:]))
    
    # Sử dụng dictionary để lưu {giá trị: chỉ số}
    s = {}
    
    for j in range(n):
        complement = t - a[j]
        
        # Nếu phần bù (target - số hiện tại) đã xuất hiện trước đó
        if complement in s:
            # In ra chỉ số của phần bù (i) và chỉ số hiện tại (j)
            print(s[complement], j)
            return
            
        # Nếu chưa thấy, lưu số hiện tại và chỉ số của nó vào dict
        s[a[j]] = j

if __name__ == "__main__":
    solve()