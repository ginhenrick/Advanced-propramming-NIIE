class HinhHoc:
    def __init__(self):
        self.DienTich = 0
        self.ChuVi = 0

    def TinhDienTichChuVi(self):
        pass

class HinhChuNhat:
    dai: float = 0
    rong: float = 0

    def __init__(self,d,r) -> None:
        self.dai = d
        self.rong = r

    def tinhdientichchuvi(self):
        self.dientich = self.dai * self.rong
        self.chuvi = (self.dai + self.rong)*2

    def __str__(self) -> str:
        return f"HCN {self.dai}x{self.rong} có S = {self.dientich}, P = {self.chuvi}"