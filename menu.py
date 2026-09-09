def menu():
    print("\n" + "=" * 40)
    print("STUDENT MANAGEMENT WITH SQL & OOP")
    print("=" * 40)
    print("1.ADD STUDENT")
    print("2.SELECT STUDENT")
    print("3.VIEW ALL STUDENTS")
    print("4.DELETE STUDENT")
    print("5.EXIT")

    for attempt in range(3):
        try:
            choice = int(input("ENTER OPTION (1-5): "))
            if 1 <= choice <= 5:
                return choice
            print(f"Enter a valid option({attempt + 1}/3): ")
        except ValueError:
            print(f"Enter a valid Digit({attempt + 1}/3): ")
    print("Failed on Attempts")
    return None


def student_menu():
    print("\n" + "=" * 40)
    print("STUDENT SELECTION MENU")
    print("=" * 40)
    print("1.ADD GRADE")
    print("2.CALCULATE AVERAGE")
    print("3.UPDATE")
    print("4.VIEW STUDENT PROFILE")
    print("5.EXIT")

    for attempt in range(3):
        try:
            choice = int(input("ENTER OPTION (1-5): "))
            if 1 <= choice <= 5:
                return choice
            print(f"Enter a valid option({attempt + 1}/3): ")
        except ValueError:
            print(f"Enter a valid Digit({attempt + 1}/3): ")
    print("Failed on Attempts")
    return None


def update_menu():
    print("\n" + "=" * 40)
    print("STUDENT UPDATE MENU")
    print("=" * 40)
    print("1.UPDATE COURSE GRADE")
    print("2.UPDATE NAME")
    print("3.UPDATE AGE")
    print("4.EXIT")

    for attempt in range(3):
        try:
            choice = int(input("ENTER OPTION (1-4): "))
            if 1 <= choice <= 4:
                return choice
            print(f"Enter a valid option({attempt + 1}/3): ")
        except ValueError:
            print(f"Enter a valid Digit({attempt + 1}/3): ")
    print("Failed on Attempts")
    return None
