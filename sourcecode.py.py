
students = []  # Khởi tạo danh sách sinh viên trống
def add_new_student():
    print('===== Add New Student =====')
    while True:
        id = input('Enter student ID: ')
        if any(s['ID'] == id for s in students):
            print('A student with this ID already exists. Please enter a different ID.')
        else:
            break
    name = input('Enter student name: ')
    className = input('Enter class name: ')

    # Nhập thông tin điểm số môn học
    courseMarks = {}
    while True:
        subject = input('Enter subject (or press Enter to finish): ')
        if not subject:  # Nếu người dùng không nhập gì nữa thì dừng lại
            break
        mark = float(input('Enter mark: '))
        courseMarks[subject] = mark

    # Tạo dictionary chứa thông tin sinh viên
    student = {}
    student['ID'] = id
    student['FullName'] = name
    student['ClassName'] = className
    student['CourseMarks'] = courseMarks

    # Thêm sinh viên vào danh sách
    students.append(student)

    print('Student added successfully!\n')

def view_student_list():
    print('===== View Student List =====')
    for student in students:
        print('ID:', student['ID'])
        print('FullName:', student['FullName'])
        print('ClassName:', student['ClassName'])
        print('CourseMarks:')
        print('{')
        for subject, mark in student['CourseMarks'].items():
            print(f'    Subject: {subject}, Mark: {mark}')
        print('}\n')

def update_student_info():
    print('===== Update Student Info =====')
    id = input('Search ID student to update: ')

    # Tìm sinh viên trong danh sách
    found = False
    for student in students:
        if student['ID'] == id:
            found = True
            print('Enter new information (or press Enter to skip):')
            name = input(f'Enter student name ({student["FullName"]}): ')
            className = input(f'Enter class name ({student["ClassName"]}): ')

            # Cập nhật thông tin điểm số môn học
            while True:
                subject = input('Enter subject (or press Enter to finish): ')
                if not subject:  # Nếu người dùng không nhập gì nữa thì dừng lại
                    break
                mark = input(f'Enter mark for {subject} ({student["CourseMarks"].get(subject, "")}): ')
                if mark:  # Nếu người dùng nhập điểm thì cập nhật, nếu không thì giữ nguyên
                    student['CourseMarks'][subject] = float(mark)

            if name:
                student['FullName'] = name
            if className:
                student['ClassName'] = className

            print('Student information updated successfully!\n')
            break

    if not found:
        print(f'Student with ID {id} not found.\n')


def delete_student():
    student_id = input('Enter student ID to delete: ')
    # Kiểm tra xem sinh viên có tồn tại trong danh sách sinh viên hay không
    for student in students:
        if student['ID'] == student_id:
            students.remove(student)
            print(f'Student with ID "{student_id}" has been deleted successfully.\n')
            return
    print(f'Student with ID "{student_id}" does not exist in the student list.\n')


def search_student_by_keyword():
    keyword = input('Enter keyword to search: ').lower()
    found_students = []
    for student in students:
        if keyword in student['FullName'].lower() or keyword in student['ClassName'].lower():
            found_students.append(student)

    if found_students:
        print(f'Found {len(found_students)} student(s) with keyword "{keyword}":')
        for student in found_students:
            print('ID:', student['ID'])
            print('FullName:', student['FullName'])
            print('ClassName:', student['ClassName'])
            print('CourseMarks:')
            for subject, mark in student['CourseMarks'].items():
                print('  Subject:', subject)
                print('  Mark:', mark)
            print('---')
    else:
        print(f'No student found with keyword "{keyword}".')

def sort_students():
    sort_by = input('Enter sort option (1: by ID, 2: by FullName, 3: by ClassName): ')
    if sort_by == '1':
        sorted_students = sorted(students, key=lambda x: x['ID'])
    elif sort_by == '2':
        sorted_students = sorted(students, key=lambda x: x['FullName'])
    elif sort_by == '3':
        sorted_students = sorted(students, key=lambda x: x['ClassName'])
    else:
        print('Invalid option. Please try again.')
        return

    print('Sorted student list:')
    for student in sorted_students:
        print('ID:', student['ID'])
        print('FullName:', student['FullName'])
        print('ClassName:', student['ClassName'])
        print('CourseMarks:')
        for mark in student['CourseMarks']:
            print('  Subject:', mark['Subject'])
            print('  Mark:', mark['Mark'])
        print('---')



while True:
    print('===== Student Management System =====')
    print('1. View student list (Xem danh sách sinh viên)')
    print('2. Add new student (Thêm sinh viên mới)')
    print('3. Update student info (Cập nhật thông tin sinh viên)')
    print('4. Delete student (Xóa sinh viên)')
    print('5. Search student by keyword (Tìm sinh viên theo từ khóa)')
    print('6. Sort student (Sắp xếp sinh viên)')
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
        sort_students()
    elif choice == '0':
        print('Thank you for using Student Management System. Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.\n')