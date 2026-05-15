"""Dấu ngoặc cân đối
Cho chuỗi chứa các ký tự ()[]{}.
Kiểm tra có cân đối không (mỗi ngoặc mở có ngoặc đóng cùng loại, lồng đúng).
In YES / NO."""

"""Format input / output
Input: 1 dòng chuỗi, chỉ gồm ()[]{}
Output: YES nếu cân đối, ngược lại NO"""

"""s = input()
# TODO: dùng stack — push ngoặc mở, pop khi gặp ngoặc đóng
# mismatch hoặc stack rỗng khi đóng → NO
# duyệt xong: stack rỗng → YES, ngược lại NO
# Độ phức tạp: O(n)"""

def check_balanced_brackets():
    try:
        s = input().strip()
    except EOFError:
        return

    stack = []
    # Từ điển ánh xạ ngoặc đóng với ngoặc mở tương ứng
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            # Nếu là ngoặc đóng, lấy phần tử trên cùng của stack để so khớp
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                print("NO")
                return
        else:
            # Nếu là ngoặc mở, push vào stack
            stack.append(char)

    # Sau khi duyệt hết, nếu stack rỗng là cân đối
    if not stack:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    check_balanced_brackets()