# n = int(input())

# if n == 0:
#     print(0)
# elif n == 1:
#     print(1)
# else:
#     # Khởi tạo dãy với 2 số đầu tiên
#     A = [0, 1]
#     for i in range(2, n + 1):
#         # Số tiếp theo bằng tổng 2 số trước đó
#         m = A[i - 1] + A[i - 2]
#         A.append(m)
#     print(A[n])


# def longest_palindromic_substring(s: str) -> str:
#     n = len(s)
#     if n == 0:
#         return ""
    
#     longest = s[0]  # Khởi tạo chuỗi palindromic dài nhất là ký tự đầu tiên

#     for i in range(n):
#         # Kiểm tra chuỗi palindromic có độ dài lẻ
#         left, right = i, i
#         while left >= 0 and right < n and s[left] == s[right]:
#             current_palindrome = s[left:right + 1]
#             if len(current_palindrome) > len(longest):
#                 longest = current_palindrome
#             left -= 1
#             right += 1
        
#         # Kiểm tra chuỗi palindromic có độ dài chẵn
#         left, right = i, i + 1
#         while left >= 0 and right < n and s[left] == s[right]:
#             current_palindrome = s[left:right + 1]
#             if len(current_palindrome) > len(longest):
#                 longest = current_palindrome
#             left -= 1
#             right += 1

#     return longest

# def longest_palindromic_substring(s):
#     n = len(s)
#     if n == 0:
#         return ""
#     dp = [[False] * n for _ in range(n)]
#     start = 0
#     max_length = 1
#     for i in range(n):
#         dp[i][i] = True
#     for length in range(n-1):
#         if s[i] == s[i+1]:
#             dp[i][i+1] = True
#             start = i
#             max_length = 2
#     for length in range(3, n+1):
#         for i in range(n-length+1):
#             j = i + length - 1
#             if s[i] == s[j] and dp[i+1][j-1]:
#                 dp[i][j] = True
#                 start = i
#                 max_length = length
#     return s[start:start + max_length]
# class Movie:
#     def __init__(self, title, year, director, duration):
#         if not title.strip():
#             raise ValueError('Title cannot be empty')
#         if year < 1895:
#             raise ValueError('Year must be 1895 or later')
#         if not director.strip():
#             raise ValueError('Director cannot be empty')
#         if duration <= 0:
#             raise ValueError('Duration must be positive')
#         self.title = title
#         self.year = year
#         self.director = director
#         self.duration = duration

#     def __str__(self):
#         return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'
# class MediaCatalogue:
#     def __init__(self):
#         self.items = []
#     #def add(self):

# try:
#     movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
#     print(movie1)
# except ValueError as e:
#     print(f'Validation Error: {e}')
def hanoi_solver(n):
    # Initialize the three rods
    # Rod A (index 0) starts with all disks in descending order
    # Rods B and C (indices 1 and 2) start empty
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def format_rods():
        """Helper to format the current state of rods as a string."""
        return f"{rods[0]} {rods[1]} {rods[2]}"

    # Record the initial state
    moves.append(format_rods())

    def move_disks(disks, source, target, auxiliary):
        if disks > 0:
            # Move n-1 disks from source to auxiliary rod
            move_disks(disks - 1, source, auxiliary, target)
            
            # Move the actual disk from source to target rod
            disk = rods[source].pop()
            rods[target].append(disk)
            
            # Record the state after the move
            moves.append(format_rods())
            
            # Move the n-1 disks from auxiliary to target rod
            move_disks(disks - 1, auxiliary, target, source)

    # Solve the puzzle: move n disks from rod 0 to rod 2 using rod 1
    move_disks(n, 0, 2, 1)
    
    # Return all moves joined by newlines
    return "\n".join(moves)