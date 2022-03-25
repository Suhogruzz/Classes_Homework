# Класс Студента(1:Инициализация класса 2:Оценка лектора 3:Вывод с помощью метода __str__
# 4:Сравнение средних оценок студентов)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, rated_course, grade):
        if isinstance(lecturer, Lecturer) \
                and rated_course in lecturer.courses_attached \
                and rated_course in self.courses_in_progress \
                and 0 < grade <= 10:
            lecturer.grades.append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        out = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {average_grade(self.grades)}\n'
               f'Курсы в процессе изучения: {self.courses_in_progress}\n' 
               f'Завершенные курсы: {self.finished_courses}')
        return out

    def __lt__(self, another_student):
        if isinstance(another_student, Student):
            return average_grade(self.grades) < average_grade(another_student.grades)
        else:
            return 'Вы сравниваете оценки студента и лектора!'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Класс Лектора(1:Инициализация класса 2:Вывод с помощью метода __str__ 3:Сравнение оценок средних оценок лекторов)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.courses_attached = []

    def __str__(self):
        out = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {average_grade(self.grades)}'
               )
        return out

    def __lt__(self, another_lecturer):
        if isinstance(another_lecturer, Lecturer):
            return average_grade(self.grades) < average_grade(another_lecturer.grades)
        else:
            return 'Вы сравниваете оценки студента и лектора!'

# Класс Проверяющего эксперта(1:Инициализация класса 2:Оценка студентов по курсам)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        out = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}'
               )
        return out

    def rate_hw(self, some_student, rated_course, grade):
        if isinstance(some_student, Student) \
                and rated_course in self.courses_attached \
                and rated_course in some_student.courses_in_progress:
            if rated_course in some_student.grades:
                some_student.grades[rated_course] += [grade]
            else:
                some_student.grades[rated_course] = [grade]
        else:
            return 'Ошибка'


# Функция подсчета средних оценок(общая)

def average_grade(grades):
    if type(grades) is dict:
        total_grades = []
        for values in grades.values():
            for grade in values:
                total_grades.append(grade)
        return average_grade(total_grades)
    elif type(grades) is list and grades[0] is not None:
        average = round(sum(grades) / len(grades), 2)
        return average
# Функция подсчета средних оценок студента по курсам


def average_students_grade(allstudents, current_course):
    all_course_grades = []
    for student in allstudents:
        if current_course in student.grades.keys():
            for all_grade in student.grades.get(current_course):
                all_course_grades.append(all_grade)
        else:
            print(f'Студент {student.name} {student.surname} не посещает курс {current_course}!')
    return average_grade(all_course_grades)

# Функция подсчета средних оценок лекторов по определенному курсу


def average_lecturers_grade(alllecturers, attached_course):
    all_lecturers_grades = []
    for lecturer in alllecturers:
        if attached_course in lecturer.courses_attached:
            for lecturer_grade in lecturer.grades:
                all_lecturers_grades.append(lecturer_grade)
        else:
            print(f'Лектор {lecturer.name} {lecturer.surname} не преподает {attached_course}!')
    return average_grade(all_lecturers_grades)


# Создание классов


# Студенты

student_1 = Student('Roy', 'Eman', 'Male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']
student_1.grades['Git'] = [1, 2, 3]
student_1.grades['Python'] = [10, 10]

student_2 = Student('David', 'Livesey', 'AHAHAHA')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Git']
student_2.grades['Git'] = [1, 2, 8]
student_2.grades['Java'] = [10, 10]

students = [student_1, student_2]

# Лекторы

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Once', 'Toldme')
lecturer_2.courses_attached += ['Java']

lecturers = [lecturer_1, lecturer_2]

# Проверяющие эксперты

reviewer_1 = Reviewer('Baba', 'Booey')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Solid', 'Snake')
reviewer_2.courses_attached += ['Git']
reviewer_2.courses_attached += ['Java']

# Проверки методов


# Выставление оценок студентам

reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_1.rate_hw(student_1, 'Git', 6)
print(f'Обновленные оценки студента {student_1.name} {student_1.surname}: {student_1.grades}')

reviewer_2.rate_hw(student_2, 'Python', 6)
reviewer_2.rate_hw(student_2, 'Java', 4)
reviewer_2.rate_hw(student_2, 'Git', 6)
print(f'Обновленные оценки студента {student_2.name} {student_2.surname}: {student_2.grades}')

# Выставление оценок лекторам

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Git', 7)
print(f'Оценки лектора {lecturer_1.name} {lecturer_1.surname}: {lecturer_1.grades}')

student_2.rate_lecturer(lecturer_2, 'Python', 3)
student_2.rate_lecturer(lecturer_2, 'Java', 10)
student_2.rate_lecturer(lecturer_2, 'Git', 7)
print(f'Оценки лектора {lecturer_2.name} {lecturer_2.surname}: {lecturer_2.grades}')

# Вывод классов

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)
# Проверка средних оценок


# Средние оценки студентов

course = 'Java'
print(f'Средние оценки студентов за курс {course} {average_students_grade(students, course)}')
# Средние оценки лекторов

print(f'Средние оценки лекторов за курс {course} {average_lecturers_grade(lecturers, course)}')

# Сравнения средних оценок

print(student_1 < student_2)
print(student_1 > student_2)
print(student_2 > lecturer_1)

print(lecturer_1 < lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 > student_1)