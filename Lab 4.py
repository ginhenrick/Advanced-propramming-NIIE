class Circle:
    def __init__(self, r):
        self.r = r
    def nhap(self):
        self.r = float(input("Nhập vào bán kính hình tròn: "))

    def chuvi(self):
        return 2 * 3.14 * self.r

    def dientich(self):
        return 3.14 * self.r ** 2

Circle = Circle(0)
Circle.nhap()
print("Chu vi hình tròn là:", Circle.chuvi())
print("Diện tích hình tròn là:", Circle.dientich())