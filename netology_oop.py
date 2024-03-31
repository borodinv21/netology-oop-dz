class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_homework_grade(self):
        sum = 0
        count = 0

        for value in self.grades.values():
            sum += average_grade(value)
            count += 1

        return sum / count

    def __lt__(self, other):
        return self._average_homework_grade() < other._average_homework_grade()

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
              f'Средняя оценка за лекции: {format(self._average_homework_grade(), '.1f')}\n'
              f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
              f'Завершенные курсы: {', '.join(self.finished_courses)}')


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_lections_grade(self):
        sum = 0
        count = 0

        for value in self.grades.values():
            sum += average_grade(value)
            count += 1

        return sum / count

    def __lt__(self, other):
        return self._average_lections_grade() < other._average_lections_grade()

    def __str__(self):
        return (f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}\n'
              f'Средняя оценка за лекции: {format(self._average_lections_grade(), '.1f')}')


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
        return (f'Имя: {self.name}\nФамилия: {self.surname}')

def average_grade(grades):
    sum = 0
    count = 0

    if len(grades) < 2:
        sum += int(*grades)
        count += 1
    else:
        for i in grades:
            sum += i
            count += 1

    return sum / count

def get_average_grade(grades):
    sum = 0
    count = 0

    sum += average_grade(grades)
    count += 1

    return (sum, count)

def general_average_grade(objects, course):
    sum = 0
    count = 0

    student = True

    if not isinstance(objects[0], Student):
        student = False

    if student:
        for i in objects:
            if course in i.courses_in_progress:
                sum, count = get_average_grade(i.grades[course])

    else:
        for i in objects:
            if course in i.courses_attached:
                sum, count = get_average_grade(i.grades[course])

    return sum / count


#----------------Класс студента и ревьюера и работа с методами--------------------
reviewer1 = Reviewer('Мария', 'Данилова')
reviewer2 = Reviewer('Антон', 'Антонов')

reviewer1.courses_attached.append('Python')
reviewer1.courses_attached.append('Java')
reviewer2.courses_attached.append('Python')
reviewer2.courses_attached.append('Java')

student1 = Student('Иван', 'Иванов', 'Мужчина')
student2 = Student('Екатерина', 'Петрова', 'Женщина')

student1.courses_in_progress.append('Python')
student1.finished_courses.append('Java')

student2.courses_in_progress.append('Java')
student2.finished_courses.append('Python')

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Java', 8)
reviewer1.rate_hw(student2, 'Python', 5)
reviewer1.rate_hw(student2, 'Java', 6)

reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student1, 'Java', 9)
reviewer2.rate_hw(student2, 'Python', 4)
reviewer2.rate_hw(student2, 'Java', 5)

print('-------------Студенты и ревьюеры-------------', end='\n' * 2)
print(student1, end='\n' * 2)
print(student2, end='\n' * 2)
print(reviewer1, end='\n' * 2)
print(reviewer2, end='\n' * 2)
print(student2 < student1, end='\n' * 3)
#----------------------------------------------------------------------

#------------------Класс лекторов и работа с методами-----------------

lecturer1 = Lecturer('Петр', 'Петров')
lecturer2 = Lecturer('Дмитрий', 'Дмитриев')

lecturer1.courses_attached.append('Python')
lecturer1.courses_attached.append('Java')

lecturer2.courses_attached.append('Java')
lecturer2.courses_attached.append('Python')

student1.rate_lecturer(lecturer1, 'Python', 8)
student2.rate_lecturer(lecturer1, 'Java', 8)
student2.rate_lecturer(lecturer1, 'Java', 9)

student1.rate_lecturer(lecturer2, 'Python', 5)
student2.rate_lecturer(lecturer2, 'Java', 10)
student2.rate_lecturer(lecturer2, 'Java', 6)

print('-------------Лекторы-------------', end='\n' * 2)
print(lecturer1, end='\n' * 2)
print(lecturer2, end='\n' * 2)
print(lecturer2 < lecturer1, end='\n' * 3)
#----------------------------------------------------------------------

#-------------Функции для подсчета средней оценки за лекции------------
print('---Средние оценки за лекции---')
print('Студенты:', general_average_grade([student1, student2], 'Python'))
print('Лекторы:', general_average_grade([lecturer1, lecturer2], 'Python'))





#Результат вывода на консоль

# -------------Студенты и ревьюеры-------------
#
# Имя: Иван
# Фамилия: Иванов
# Средняя оценка за лекции: 9.5
# Курсы в процессе изучения: Python
# Завершенные курсы: Java
#
# Имя: Екатерина
# Фамилия: Петрова
# Средняя оценка за лекции: 5.5
# Курсы в процессе изучения: Java
# Завершенные курсы: Python
#
# Имя: Мария
# Фамилия: Данилова
#
# Имя: Антон
# Фамилия: Антонов
#
# True
#
#
# -------------Лекторы-------------
#
# Имя: Петр
# Фамилия: Петров
# Средняя оценка за лекции: 8.2
#
# Имя: Дмитрий
# Фамилия: Дмитриев
# Средняя оценка за лекции: 6.5
#
# True
#
#
# ---Средние оценки за лекции---
# Студенты: 9.5
# Лекторы: 5.0