"""Đổi tiền tối thiểu — DP
Cho K mệnh giá và số tiền N.
Tìm số tờ tiền TỐI THIỂU để đổi đủ N (không giới hạn số lần dùng mỗi mệnh giá).
Nếu không đổi được, in -1."""

"""Format input / output
Input: dòng 1 K N (1 ≤ K ≤ 100, 0 ≤ N ≤ 10000), dòng 2 là K mệnh giá (int dương)
Output: số tờ tối thiểu, hoặc -1 nếu không đổi được"""

# k, n = map(int, input().split())
# coins = list(map(int, input().split()))
# # TODO: DP — dp[i] = min tờ để đổi i đồng
# # dp[0] = 0; dp[i] = min(dp[i-c]) + 1 với c in coins, i >= c
# # in -1 nếu dp[n] = INF

import sys

def solve():
    # Đọc dữ liệu từ stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    n = int(input_data[1])
    coins = list(map(int, input_data[2:]))

    # Khởi tạo mảng DP với giá trị vô cùng (float('inf'))
    # dp[i] là số tờ ít nhất để đổi được số tiền i
    dp = [float('inf')] * (n + 1)
    dp[0] = 0 # Số tờ để đổi 0 đồng là 0

    # Duyệt qua từng số tiền từ 1 đến n
    for i in range(1, n + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Nếu giá trị vẫn là vô cùng thì không đổi được
    if dp[n] == float('inf'):
        print("-1")
    else:
        print(dp[n])

if __name__ == "__main__":
    solve()