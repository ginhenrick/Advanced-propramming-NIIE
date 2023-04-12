import json

data_file = 'students.json'
students = []


def load_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {'students': []}
    return data

def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)

def print_student(student):
    print(f"ID: {student['id']}")
    print(f"Full name: {student['fullName']}")
    print(f"Class name: {student['className']}")
    print("Course marks:")
    for course, mark in student['courseMarks'].items():
        print(f"  {course}: {mark}")

def view_student_list(data):
    for student in data['students']:
        print_student(student)
        print()

def add_new_student(data):
    student = {}
    student['id'] = len(data['students']) + 1
    student['fullName'] = input("Enter full name: ")
    student['className'] = input("Enter class name: ")
    student['courseMarks'] = {}
    for course in ['math', 'physics', 'chemistry']:
        student['courseMarks'][course] = float(input(f"Enter {course} mark: "))
    data['students'].append(student)
    save_data(data)
    print("Student added successfully.")

def update_student_info(data):
    student_id = int(input("Enter student ID: "))
    for student in data['students']:
        if student['id'] == student_id:
            print_student(student)
            print()
            field = input("Enter field to update (fullName, className, math, physics, chemistry): ")
            if field in ['fullName', 'className']:
                student[field] = input(f"Enter new {field}: ")
            elif field in ['math', 'physics', 'chemistry']:
                student['courseMarks'][field] = float(input(f"Enter new {field} mark: "))
            else:
                print("Invalid field.")
                return
            save_data(data)
            print("Student info updated successfully.")
            return
    print("Student not found.")

def delete_student(data):
    student_id = int(input("Enter student ID: "))
    for i, student in enumerate(data['students']):
        if student['id'] == student_id:
            del data['students'][i]
            save_data(data)
            print("Student deleted successfully.")
            return
    print("Student not found.")

def search_student_by_keyword(data):
    keyword = input("Enter keyword to search: ")
    for student in data['students']:
        if keyword in student['fullName'] or keyword in student['className']:
            print_student(student)
            print()
    print("Search finished.")

def sort_student(data):
    field = input("Enter field to sort by (fullName, className, math, physics, chemistry): ")
    if field in ['fullName', 'className']:
        data['students'].sort(key=lambda x: x[field])
    elif field in ['math', 'physics', 'chemistry']:
        data['students'].sort(key=lambda x: x['courseMarks'][field])
    else:
        print("Invalid field.")
        return
    print("Student list sorted successfully.")

def main():
    data = load_data()
    while True:
        print("1: View student list")
        print("2: Add new student")
        print("3: Update student info")
        print("4: Delete student")
        print("5: Search student by keyword")
        print("6: Sort student")
        print("0: Exit program")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_student_list(data)
        elif choice == '2':
            add_new_student(data)
        elif choice == '3':
            update_student_info(data)
        elif choice == '4':
            delete_student(data)
        elif choice == '5':
            search_student_by_keyword(data)
        elif choice == '6':
            sort_student(data)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
