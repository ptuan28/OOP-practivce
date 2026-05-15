class Polynomial:
    def __init__(self, coeffs: list):
        # Lưu trữ hệ số, loại bỏ các số 0 dư thừa ở đầu (vd: [0, 0, 3, 2] -> [3, 2])
        # Tìm chỉ số đầu tiên khác 0
        first_nonzero = 0
        while first_nonzero < len(coeffs) - 1 and coeffs[first_nonzero] == 0:
            first_nonzero += 1
        self.coeffs = list(coeffs[first_nonzero:])

    def __str__(self):
        if not self.coeffs or (len(self.coeffs) == 1 and self.coeffs[0] == 0):
            return "0"
        
        res = ""
        n = len(self.coeffs) - 1  # Bậc của đa thức
        
        for i, a in enumerate(self.coeffs):
            power = n - i
            if a == 0:
                continue
            
            # Xử lý dấu
            if a > 0 and res:
                res += " + "
            elif a < 0:
                res += " - " if res else "-"
            
            # Xử lý hệ số (chỉ hiện số nếu khác 1 hoặc là bậc 0)
            abs_a = abs(a)
            if abs_a != 1 or power == 0:
                res += str(abs_a)
            
            # Xử lý biến x và bậc
            if power > 0:
                res += "x"
                if power > 1:
                    res += f"^{power}"
        return res

    def __call__(self, x):
        # Sử dụng thuật toán Horner: b = a_n + x * b
        result = 0
        for coeff in self.coeffs:
            result = result * x + coeff
        return result

    def __add__(self, other):
        # Lấy độ dài lớn nhất để align hệ số
        len1, len2 = len(self.coeffs), len(other.coeffs)
        max_len = max(len1, len2)
        
        # Padding thêm số 0 vào bên trái để cùng độ dài
        c1 = [0] * (max_len - len1) + self.coeffs
        c2 = [0] * (max_len - len2) + other.coeffs
        
        # Cộng tương ứng các hệ số
        new_coeffs = [a + b for a, b in zip(c1, c2)]
        return Polynomial(new_coeffs)