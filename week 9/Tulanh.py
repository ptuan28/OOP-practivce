class TuLanh:
    def __init__(self, 
                 brand: str = "Elextrolux", 
                 id: str = 'UNKNOWN', 
                 origin: str = 'VIETNAM', 
                 inverterFound: bool = True, 
                 amountHeld: int = 256, 
                 price: int = 7000000):
        self.__brand = brand
        self.__id = id
        self.__origin = origin
        self.__inverterFound = inverterFound
        self.__amountHeld = amountHeld
        self.__price = price

    def nhapThongTin(self):
        self.__brand = input()
        self.__id = input()
        self.__origin = input()

        inverter_input = input().lower()
        self.__inverterFound = True if inverter_input in ['true', '1', 'có', 'yes'] else False
        self.__amountHeld = int(input())
        self.__price = int(input())

    def __str__(self):
        inverter_str = "Có" if self.__inverterFound else "Không"
        return (f"Nhãn hiệu: {self.__brand}\n"
                f"Mã số: {self.__id}\n"
                f"Nước SX: {self.__origin}\n"
                f"T/K điện: {inverter_str}\n"
                f"Dung tích: {self.__amountHeld}L\n"
                f"Giá: {self.__price}VNĐ\n"
                f"Giá trung bình: {self.giaMoiLit():.0f}VNĐ/L")

    @classmethod
    def makeCopy(cls, fridge):
        return cls(fridge.__brand, fridge.__id, fridge.__origin, 
                   fridge.__inverterFound, fridge.__amountHeld, fridge.__price)

    def tinhGiaSauGiamGia(self, phanTramGiam: float):
        if phanTramGiam < 0 or phanTramGiam > 100:
            raise ValueError("Phần trăm giảm giá phải nằm trong khoảng 0 đến 100")
        return int(self.__price * (100 - phanTramGiam) / 100)

    def giaMoiLit(self):
        if self.__amountHeld <= 0:
            return 0
        return self.__price / self.__amountHeld
