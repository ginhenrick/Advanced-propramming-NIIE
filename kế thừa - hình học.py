class HinhHoc:
    def __init__(self):
        self.DienTich = 0
        self.ChuVi = 0

    def TinhDienTichChuVi(self):
        pass

class HinhTron(HinhHoc):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def TinhDienTichChuVi(self):
        self.DienTich = 3.14 * self.r * self.r
        self.ChuVi = 2 * 3.14 * self.r

class HinhChuNhat(HinhHoc):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def TinhDienTichChuVi(self):
        self.DienTich = self.a * self.b
        self.ChuVi = 2 * (self.a + self.b)

HinhTron = HinhTron(6)
HinhTron.TinhDienTichChuVi()
print("Hinh tron co dien tich la", HinhTron.DienTich, "va chu vi la", HinhTron.ChuVi)

HinhChuNhat = HinhChuNhat(2, 5)
HinhChuNhat.TinhDienTichChuVi()
print("Hinh chu nhat co dien tich la", HinhChuNhat.DienTich, "va chu vi la", HinhChuNhat.ChuVi)

