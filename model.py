class Subject:
    def __init__(self, name, credits):
        self._name = name
        self._credits = credits

    @property
    def name(self):
        return self._name

    @property
    def credits(self):
        return self._credits

    def __str__(self):
        return f"{self.name} (Credits: {self.credits})"


class Math(Subject):
    def __init__(self):
        super().__init__("Math", 4)


class Science(Subject):
    def __init__(self):
        super().__init__("Science", 4)


class English(Subject):
    def __init__(self):
        super().__init__("English", 4)


class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__subjects = []
        self.__grades = {}

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    def add_subject(self, subject):
        if subject.name not in self.__subjects:
            self.__subjects.append(subject)

    def set_grade(self, subject, grade):
        if subject in self.__subjects:
            self.__grades[subject.name] = grade
        else:
            return "Student is not registered in this subject"

    def get_grade(self, subject):
        return self.__grades.get(subject.name, "No score available")

    def calculate_average(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades.values()) / len(self.__grades)

    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}")
        print("Registered subject:")
        for subject in self.__subjects:
            print(f"- {subject.name}")
        print("Score:")
        for subject, grade in self.__grades.items():
            print(f"- {subject}: {grade}")
        print(f"Average score: {self.calculate_average()}\n")