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
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_homework_grade(self):
        sum = 0
        count = 0

        for key, value in self.grades.items():
            sum += value
            count += 1

        return sum / count

    def __lt__(self, other):
        return self._average_homework_grade() < other._average_homework_grade()

    def __str__(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}\n'
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

        for key, value in self.grades.items():
            sum += value
            count += 1

        return sum / count

    def __lt__(self, other):
        return self._average_lections_grade() < other._average_lections_grade()

    def __str__(self):
        print(f'Имя: {self.name}\n'
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
        print(f'Имя: {self.name}\nФамилия: {self.surname}')
