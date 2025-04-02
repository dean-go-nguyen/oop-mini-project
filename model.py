class Subject:
    def __init__(self, name, teacher, credits):
        self.name = name
        self.teacher = teacher
        self.credits = credits
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return [student.name for student in self.students]

    def __str__(self):
        return f"{self.name} (Teacher: {self.teacher})"


class Math(Subject):
    def __init__(self, teacher):
        super().__init__("Math", teacher, 4)


class Science(Subject):
    def __init__(self, teacher):
        super().__init__("Science", teacher, 4)


class English(Subject):
    def __init__(self, teacher):
        super().__init__("English", teacher, 4)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = []
        self.grades = {}

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
            subject.add_student(self)

    def set_grade(self, subject, grade):
        if subject in self.subjects:
            self.grades[subject.name] = grade
        else:
            return "Student is not registered to this subject"

    def get_grade(self, subject):
        return self.grades.get(subject.name, "No score available")

    def calculate_average(self):
        if not self.grades:
            return "No data to calculate"
        return sum(self.grades.values()) / len(self.grades)

    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}")
        print("Registered subject:")
        for subject in self.subjects:
            print(f"- {subject.name} (Teacher: {subject.teacher})")
        print("Score:")
        for subject, grade in self.grades.items():
            print(f"- {subject}: {grade}")
        print(f"Average score: {self.calculate_average()}\n")