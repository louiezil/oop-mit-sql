def get_age():
    for attempt in range(3):
        try:
            age = int(input("Enter Age(18-45): "))
            if 18 <= age <= 45:
                return age
            print(f"Enter valid age ({attempt + 1}/3)")
        except ValueError:
            print(f"Enter valid Digit ({attempt + 1}/3)")
    print("Failed on Attempts")
    return None


def get_grade():
    for attempt in range(3):
        try:
            grade = int(input("Enter grade(0-100): "))
            if 0 <= grade <= 100:
                return grade
            print(f"Enter valid Grade ({attempt + 1}/3)")
        except ValueError:
            print(f"Enter valid Digit ({attempt + 1}/3)")
    print("Failed on Attempts")
    return None


def get_name():
    for attempt in range(3):
        name = input("Enter Name:").strip().capitalize()
        if not name:
            print(f"Name Can't be Empty ({attempt + 1}/3)")
            continue
        return name
    print("Failed on Attempts")
    return None


def find_student(cursor, name):
    try:
        cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        student = cursor.fetchone()
        if not student:
            return None
        return student
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_course():
    for attempt in range(3):
        course = input("Enter Course: ").strip().capitalize()
        if not course:
            print(f"Course cant be Empty ({attempt + 1}): ")
            continue
        return course
    print("Failed on Attempts")
    return None


def find_course(cursor, student_id, course):
    try:
        cursor.execute(
            "SELECT * FROM grades WHERE course =? AND student_id =? ",
            (
                course,
                student_id,
            ),
        )
        result = cursor.fetchone()
        if not result:
            print(f"No Course with the Name:{course} was found")
            return None
        return result
    except Exception as e:
        print(f"error:{e}")
        return None


def view_all(cursor):
    all_averages = []
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    if not result:
        print("No Student in data")
        return None
    for student_id, name, age in result:
        print("\n" + "=" * 40)
        print(f"Name:{name}")
        print(f"Age:{age}")
        print(f"ID:{student_id}")
        # grades
        try:
            cursor.execute(
                "SELECT course,grade FROM grades WHERE student_id=?", (student_id,)
            )
            grades = []
            for course, grade in cursor.fetchall():
                grades.append(grade)
                print(f"{course}:{grade}")
            if 1 <= len(grades):
                avg = sum(grades) / len(grades)
                all_averages.append(avg)
                print(f"Avg:{avg:.2f}")

        except Exception as e:
            print(f"error:{e}")
            return None

    T_average = sum(all_averages) / len(all_averages)
    print("=" * 40)
    print(f"Number of Students:({len(result)})")
    print(f"Class Average Statistic:{T_average:.2f}")
    print("=" * 40)


def delete(name, cursor, conn):
    cursor.execute("DELETE FROM students WHERE name = ?", (name,))
    conn.commit()
    print(f"{name} deleted sucess")
