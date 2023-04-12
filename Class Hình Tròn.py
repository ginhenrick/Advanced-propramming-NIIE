class HinhHoc:
    def __init__(self):
        self.DienTich = 0
        self.ChuVi = 0

    def TinhDienTichChuVi(self):
        pass

class HinhTron:
    bankinh: float = 0

    def __index__(self,r) -> None:
        self.bankinh = r

    def tinhdientichchuvi(self):
        self.dientich = 3.14 * self.r * self.r
        self.chuvi = 2 * 3.14 * self.r

    def __str__(self) -> str:
        return f"HinhTron {self.bankinh} co S = {self.dientich}, P = {self.chuvi}"