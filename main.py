from model import Math, Science, Student, English

if __name__ == "__main__":
    math = Math()
    science = Science()
    english = English()

    alice = Student("Alice", 20)
    bob = Student("Bob", 22)

    alice.add_subject(math)
    alice.add_subject(science)

    alice.set_grade(math, 9)
    alice.set_grade(science, 8.5)

    bob.add_subject(english)
    bob.set_grade(english, 9.5)

    alice.display_info()
    bob.display_info()

    print(alice.get_grade(math))
    print(bob.get_grade(English()))