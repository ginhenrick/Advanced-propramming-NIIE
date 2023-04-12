#import HinhHoc
from HinhHoc import HinhHoc, HinhChuNhat, HinhTron

arr = []
#Hardcode

arr.append(HinhChuNhat(7,5,2))
arr.append(HinhTron(7.7))
arr.append(HinhTron(99))
arr.append(HinnChuNhat(101,13))

for item in arr:
    item.tinhdientichchuvi()
    print(item)