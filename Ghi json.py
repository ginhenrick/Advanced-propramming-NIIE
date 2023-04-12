import json

# Khởi tạo danh sách các sinh viên trong lớp
students = [
    {'name': 'John', 'age': 18, 'gender': 'male', 'grade': 9},
    {'name': 'Jane', 'age': 17, 'gender': 'female', 'grade': 10},
    {'name': 'David', 'age': 16, 'gender': 'male', 'grade': 11},
    {'name': 'Emma', 'age': 18, 'gender': 'female', 'grade': 9},
    {'name': 'Michael', 'age': 17, 'gender': 'male', 'grade': 10},
    {'name': 'Sophia', 'age': 16, 'gender': 'female', 'grade': 11},
]

# Ghi danh sách sinh viên dưới dạng JSON vào file quản lý
with open('15-4-deadline-NEW-FIXED.py', 'w') as file:
    json.dump(students, file)
with open('15-4-deadline-NEW-FIXED.py', 'r') as file:
    data = file.read()