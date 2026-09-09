class Student:
    def __init__(self, name, age, student_id=None):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = {}

    def save_student(self, cursor, conn):
        if self.student_id is None:
            try:
                print(f"Saving Data Executed for student:{self.name}...")
                cursor.execute(
                    "INSERT INTO students(name,age)VALUES(?,?)",
                    (
                        self.name,
                        self.age,
                    ),
                )
                conn.commit()
                # lets get the id from the saved data and replace it here
                cursor.execute("SELECT id FROM students WHERE name =?", (self.name,))
                result = cursor.fetchone()
                self.student_id = result[0]
                print(f"student:{self.name} Saved Successfully into Database")
                return True
            except Exception as e:
                if "locked" in str(e):
                    print(f"{self.name} Already Exist In Database")
                    return False
        else:
            try:
                cursor.execute(
                    "UPDATE students SET name=?,age=? WHERE id=?",
                    (
                        self.name,
                        self.age,
                        self.student_id,
                    ),
                )
                conn.commit()
                print(f"student:{self.name} Updated Successfully into Database")
                return True
            except Exception as e:
                print(f"Error: {e}")

                return False

    def add_grade(self, cursor, conn, course, grade):
        if not self.student_id:
            print(f"student not saved into Database")
            return False

        print("Grade Saving Executed ")
        try:
            cursor.execute(
                "INSERT INTO grades(course,grade,student_id)VALUES(?,?,?)",
                (
                    course,
                    grade,
                    self.student_id,
                ),
            )
            conn.commit()
            self.grades[course] = grade
            print(f"Loaded and Saved Grade Successfully")
            return True
        except Exception as e:
            print(f"error: {e}")
            return False

    def load_grades(self, cursor):
        self.grades = {}
        if self.student_id is None:
            print("student not saved to the database")
            return False

        # serch for the grades using the id from the student
        print(f"Loading Grades for '{self.name}'")
        try:
            cursor.execute(
                "SELECT course,grade FROM grades WHERE student_id = ?",
                (self.student_id,),
            )
            result = cursor.fetchall()
            for course, grade in result:
                self.grades[course] = grade
            print(f"Loaded {len(self.grades)} Grades into '{self.name}'")
            return True
        except Exception as e:
            print(f"Error:{e}")
            return None

    def average(self):
        if not self.grades:
            avg = 0
            return avg
        grades = self.grades.values()
        courses = self.grades.keys()
        avg = sum(grades) / len(courses)
        return avg

    def display(self):
        print("\n" + "=" * 40)
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"ID: {self.student_id}")
        if self.grades:
            for course, grade in self.grades.items():
                print(f"{course}: {grade}")
        else:
            print("[_____]:[_____]")
        avg = self.average()
        if avg:
            print(f"Avg:{avg:.2f}")
        else:
            print("avg:[______]")
        print("=" * 40)

    def update_course(self, cursor, conn, course, new_grade):
        try:
            cursor.execute(
                "UPDATE grades SET grade=? WHERE student_id =? AND course =? ",
                (
                    new_grade,
                    self.student_id,
                    course,
                ),
            )
            conn.commit()
            self.load_grades(cursor)
            print(f"{course} Grade Updated to {new_grade} successfully")
            return True
        except Exception as e:
            print(f"error:{e}")
            return False

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age
