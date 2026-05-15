"""
Chuỗi con đối xứng dài nhất
Cho chuỗi s. Tìm chuỗi con liên tiếp dài nhất mà đối xứng (s[i..j] == reverse(s[i..j])). 
In chuỗi đó — nếu có nhiều đáp án cùng độ dài, in đáp án xuất hiện sớm nhất."""

# Format input / output
# Input: 1 dòng chuỗi không rỗng, 1 ≤ |s| ≤ 1000
# Output: chuỗi con đối xứng dài nhất

"""khung code mẫu"""
# s = input()
# TODO: duyệt mọi cặp (i, j), check palindrome, lưu max
# Hint: expand around center — mỗi center (i hoặc i,i+1), mở rộng 2 bên
# Độ phức tạp: O(n^2)


def longest_palindrome():
    try:
        s = input().strip()
    except EOFError:
        return

    if not s:
        return

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Trường hợp chuỗi đối xứng lẻ (ví dụ: "aba")
        p1 = expand(i, i)
        if len(p1) > len(longest):
            longest = p1
            
        # Trường hợp chuỗi đối xứng chẵn (ví dụ: "abba")
        p2 = expand(i, i + 1)
        if len(p2) > len(longest):
            longest = p2

    print(longest)

if __name__ == "__main__":
    longest_palindrome()