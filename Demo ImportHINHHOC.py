from math import pow, pi
class Hinhhoc:
    dien_tich: float = 0
    chu_vi: float = 0

    def __str__(self) -> str:
        return "Hình học"

    def tinh_dien_tich(self):
        pass

class HinhChuNhat(Hinhhoc):
    dai: float = 0
    rong: float = 0

    def __init__(self,d,r) -> None:
        self.dai = d
        self.rong = r

    def tinh_dien_tich(self) -> None:
        self.dien_tich = self.dai * self.rong
        self.chu_vi = (self.dai + self.rong) * 2

    def __str__(self) -> str:
        return f"HCN {self.dai}x{self.rong} co S = {self.dien_tich}, P = {self.chu_vi}"

class HinhTron(Hinhhoc):
    ban_kinh: float = 0

    def __init__(self, bk) -> None:
        self.ban_kinh = bk

    def tinh_dien_tich(self) -> None:
        self.dien_tich_hr = pow(self.ban_kinh,2) * pi
        self.chu_vi_hr = (self.ban_kinh * 2) * pi

    def __str__(self) -> str:
        return f"HTR {self.ban_kinh} co S = {self.dien_tich_hr}, P = {self.chu_vi_hr}"