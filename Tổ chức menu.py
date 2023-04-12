student_information = {}

def them_thongtin_sinhvien():
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    student_information[student_id] = {'Tên': name, 'Tuổi': age}

def xuat_thongtin_sinhvien(student_id):
    print(student_information[student_id])

while True:
    print("Menu")
    print("1. Them thong tin sinh vien")
    print("2. Xuat thong tin sinh vien")
    print("3. Thoat")
    choice = int(input("Nhap vao lua chon: "))
    if choice == 1:
        them_thongtin_sinhvien()
    elif choice == 2:
        student_id = int(input("Nhap student ID: "))
        xuat_thongtin_sinhvien(student_id)
    elif choice == 3:
        break
