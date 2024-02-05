class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lct(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        self.av_grade = 0
        for value in self.grades.values():
            self.av_grade += sum(value) / len(value)
        return self.av_grade

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.average_grade()}\n'
            f'Курсы в процессе обучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        )

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        self.av_grade = 0
        for value in self.grades.values():
            self.av_grade += sum(value) / len(value)
        return self.av_grade

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.average_grade()}'
        )

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}'
        )


first_student = Student('Ruoy', 'Eman', 'your_gender')
second_student = Student('Ivan', 'Smirnov', 'man')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
first_student.finished_courses += ['Введение в программирование']
second_student.courses_in_progress += ['Python']

first_mentor = Mentor('Some', 'Buddy')
first_mentor.courses_attached += ['Python']
second_mentor = Mentor('Boris', 'Kuper')
second_mentor.courses_attached += ['Python']

first_lecturer = Lecturer('Some', 'Buddy')
first_lecturer.courses_attached += ['Python']
second_lecturer = Lecturer('Vladislav', 'Trezubov')
second_lecturer.courses_attached += ['Python']

first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python']
second_reviewer = Reviewer('Maxim', 'Belov')
second_reviewer.courses_attached += ['Python']

first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 10)

first_reviewer.rate_hw(second_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 9)

first_student.rate_lct(first_lecturer, 'Python', 10)
first_student.rate_lct(first_lecturer, 'Python', 9)

first_student.rate_lct(second_lecturer, 'Python', 8)
first_student.rate_lct(second_lecturer, 'Python', 9)

print(first_student.grades)
print(second_student.grades)
print(first_lecturer.grades)

print(first_student)
print(first_lecturer)
print(first_reviewer)

print(first_student == second_student)
print(first_student > second_student)
print(first_student < second_student)

print(first_lecturer == second_lecturer)
print(first_lecturer > second_lecturer)
print(first_lecturer < second_lecturer)

students = [first_student, second_student]
course_ = 'Python'


def middle_range_student(students, course_):
    sum = 0
    for student in students:
        if course_ in student.courses_in_progress:
            average = student.average_grade()
            sum += average
    middle = sum / len(students)
    return middle


print(middle_range_student(students, course_))

lecturers = [first_lecturer, second_lecturer]
course_ = 'Python'


def middle_range_lecturer(lecturers, course_):
    sum = 0
    for lecturer in lecturers:
        if course_ in lecturer.courses_attached:
            average = lecturer.average_grade()
            sum += average
    middle = sum / len(lecturers)
    return middle


print(middle_range_lecturer(lecturers, course_))