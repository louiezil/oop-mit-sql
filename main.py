from menu import menu, student_menu, update_menu
from database import conn_cursor, create_table, close_conn
from student import Student
from student_opps import (
    get_name,
    get_age,
    get_grade,
    find_student,
    get_course,
    find_course,
    view_all,
    delete,
)


def main():
    conn, cursor = conn_cursor()
    create_table(conn, cursor)

    while True:
        choice = menu()
        if choice == 1:
            name = get_name()
            if name is None:
                continue
            age = get_age()
            if age is None:
                continue
            student = Student(name, age)
            saved = student.save_student(cursor, conn)
            if saved is False:
                continue
            student.display()
        elif choice == 2:
            name = get_name()
            if not name:
                continue
            student_data = find_student(cursor, name)
            if student_data is None:
                print(f"{name} not found in Databse")
                continue
            student = Student(name, age=student_data[2], student_id=student_data[0])
            student.load_grades(cursor)
            student.display()
            while True:
                choice = student_menu()
                if choice == 1:
                    course = get_course()
                    if course is None:
                        continue
                    grade = get_grade()
                    if grade is None:
                        continue
                    student.add_grade(cursor, conn, course, grade)
                elif choice == 2:
                    avg = student.average()
                    if avg is None:
                        print(f"No Grades Saved to {name}")
                        continue
                    print(f"Avg: {avg:.2f}")
                elif choice == 3:
                    while True:
                        update_choice = update_menu()
                        if update_choice == 1:
                            course = get_course()
                            if course is None:
                                continue
                            verify_course = find_course(cursor, student_data[0], course)
                            if verify_course is None:
                                continue
                            new_grade = get_grade()
                            if new_grade is None:
                                continue
                            student.update_course(cursor, conn, course, new_grade)
                        elif update_choice == 2:
                            new_name = get_name()
                            student.set_name(new_name)
                            student.save_student(cursor, conn)
                        elif update_choice == 3:
                            new_age = get_age()
                            student.set_age(new_age)
                            student.save_student(cursor, conn)
                        elif update_choice == 4:
                            break
                        else:
                            print("Enter valid Option...")
                elif choice == 4:
                    student.display()
                elif choice == 5:
                    break
                else:
                    print("Enter valid option...")
        elif choice == 3:
            view_all(cursor)
        elif choice == 4:
            name = get_name()
            if name is None:
                continue
            student = find_student(cursor, name)
            if student is None:
                print(f"{name} not found in database")
                continue
            confirm = input(f"yes/n ...Do you want to delete student[{name}]: ").lower()
            if confirm == "yes":
                delete(name, cursor, conn)
            else:
                print("deletion Aborted...")
                continue
        elif choice == 5:
            break


if __name__ == "__main__":
    main()
