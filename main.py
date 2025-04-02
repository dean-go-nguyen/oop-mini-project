from model import Math, Science, Student, English

if __name__ == "__main__":
    math = Math(teacher="Mr Walter")
    science = Science(teacher="Mr White")
    english = English(teacher="Mr Black")
    student = Student("John Doe", "S12345")

    alice = Student("Alice", 20)
    bob = Student("Bob", 22)

    alice.add_subject(english)
    alice.add_subject(science)

    alice.set_grade(math, 90)
    alice.set_grade(science, 85)

    bob.set_grade(english, 95)
    bob.set_grade(science, 88)

    alice.display_info()
    bob.display_info()

    print(f"Students list in subject {math.name}: {math.get_students()}")
    print(f"Students list in subject {science.name}: {science.get_students()}")
    print(f"Students list in subject {english.name}: {english.get_students()}")