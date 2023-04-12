import json

records = [
	{
		"fullName": "Nguyễn Văn Tèo",
		"className": "21BITV04",
		"id": 2100006678,
		"courseMarks": [
			{
				"subject": "toán",
				"mark": 9.9,
			},
            {
				"subject": "lý",
				"mark": 7.9,
			}
		],
        "average": 8.9
	}
]


data_file = 'students.json'
students = []

def load_data():
    global students
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            students = json.load(f)
    except FileNotFoundError:
        pass

def save_data():
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(students, f, indent=4,ensure_ascii=False)

def get_student_by_id(student_id):
    for student in students:
        if student['id'] == student_id:
            return student
    return None

def view_student_list():
	print('List of all students:')
	print(json.dumps(records,indent=4,ensure_ascii=False))
	for student in students:
		new_dict = {
    		"fullName": student["fullName"],
    		"className": student["className"],
    		"id": student["id"],
    		"courseMarks": student["courseMarks"],
    		"average": round(sum([mark["mark"] for mark in student["courseMarks"]])/len(student["courseMarks"]), 1)
					}
		json_string = json.dumps(new_dict,indent=4,ensure_ascii=False)
		print(json_string)
		with open ("Student.json","w",encoding="utf8") as file:
    			json.dump(records,file,indent=4,ensure_ascii=False)
    

def add_new_student():
    print('Add a new student:')
    fullName = input('Full Name: ')
    className = input('Class Name: ')
    student_id = int(input('Student ID: '))
    courseMarks = []
    while True:
        subject = input('Subject (leave empty to stop): ')
        if not subject:
            break
        mark = float(input('Mark: '))
        courseMarks.append({'subject': subject, 'mark': mark})
    students.append({'id': student_id, 'fullName': fullName, 'className': className, 'courseMarks': courseMarks})
    save_data()
    print('Student added successfully.')

def update_student_info():
    print('Update student info:')
    student_id = int(input('Student ID: '))
    student = get_student_by_id(student_id)
    if not student:
        print('Student not found.')
        return
    fullName = input(f'Full Name ({student["fullName"]}): ') or student['fullName']
    className = input(f'Class Name ({student["className"]}): ') or student['className']
    courseMarks = student['courseMarks']
    while True:
        subject = input('Subject (leave empty to stop): ')
        if not subject:
            break
        mark = float(input('Mark: '))
        courseMarks.append({'subject': subject, 'mark': mark})
    student.update({'fullName': fullName, 'className': className, 'courseMarks': courseMarks})
    save_data()
    print('Student info updated successfully.')

def delete_student():
    print('Delete a student:')
    student_id = int(input('Student ID: '))
    student = get_student_by_id(student_id)
    if not student:
        print('Student not found.')
        return
    students.remove(student)
    save_data()
    print('Student deleted successfully.')

def search_student_by_keyword():
    keyword = input('Keyword: ')
    matching_students = [student for student in students if keyword.lower() in student['fullName'].lower()]
    if not matching_students:
        print('No matching student found.')
        return
    print(f'{len(matching_students)} matching student(s) found:')
    for student in matching_students:
        print(student['fullName'], student['className'], student['id'])

def sort_student():
    sorted_students = sorted(students, key=lambda student: student['fullName'])
    print('List of all students sorted by name:')
    for student in sorted_students:
        print(student['fullName'], student['className'],student['id'])

load_data()

while True:
    print('===== Student Management System =====')
    print('1. View student list(Xem danh sách sinh viên)')
    print('2. Add new student(Thêm sinh viên mới)')
    print('3. Update student info(Cập nhật thông tin sinh viên)')
    print('4. Delete student(Xóa sinh viên)')
    print('5. Search student by keyword(Tìm sinh viên theo từ khóa)')
    print('6. Sort student(Sắp xếp sinh viên)')
    print('0. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        view_student_list()
    elif choice == '2':
        add_new_student()
    elif choice == '3':
        update_student_info()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        search_student_by_keyword()
    elif choice == '6':
        sort_student()
    elif choice == '0':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.')
