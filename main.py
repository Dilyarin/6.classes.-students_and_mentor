from datetime import datetime
import os

BASE_PATH = os.getcwd()
LOGS_DIR_NAME = 'logs'
LOGS_FILE_NAME = 'logs.txt'

def parametrized_decor(full_path):
    def decor(foo):
        def log_func(*args, **kwars):
            # print('Код до вызова функции')
            res = foo(*args, **kwars)
            with open(full_path, 'a', encoding='utf-8') as file_obj:
                result = f"Вызов функции {foo.__name__}, дата и время вызова функции - {datetime.now()}, аргументы - {args}, {kwars},\n результат - {res} \n"
                # print(result)
                file_obj.write(result)
            # print('Код после вызова функции')
        return log_func
    return decor

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avr(self):
        x = 0
        for gr in self.grades.values():
            for i in gr:
                x += i
        y = x / len(gr)
        return y

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(first_student.avr(),1)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n"
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def avr(self):
        x = 0
        for gr in self.grades.values():
            for i in gr:
                x += i
        y = x / len(gr)
        return y

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(first_lecturer.avr(),1)}\n"
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('not a Student')
            return
        print(f'Оценка лекторов ниже оценки студентов: {first_lecturer.avr() < first_student.avr()}\n')


class Reviewer(Mentor):
    def __init__(self,name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\n"
        return res



first_student = Student('Ruoy', 'Eman', 'male')
first_student.courses_in_progress += ['Python', 'Git']
first_student.finished_courses = ['Введение в программирование']
second_student = Student('Kate', 'Robinson', 'female')
second_student.courses_in_progress += ['Python']

first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python']
second_reviewer = Reviewer('Some', 'Buddy2')
second_reviewer.courses_attached += ['Python']

first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(first_student, 'Python', 6)
second_reviewer.rate_hw(second_student, 'Python', 9)

first_lecturer = Lecturer('Vas', 'Ivanov')
first_lecturer.courses_attached += ['Git']
second_lecturer = Lecturer('Some', 'Buddy')
second_lecturer.courses_attached += ['Python']

first_student.rate_lect(first_lecturer, 'Git', 10)
second_student.rate_lect(first_lecturer, 'Python', 9)
first_student.rate_lect(second_lecturer, 'Git', 4)
second_student.rate_lect(second_lecturer, 'Python', 9)

@parametrized_decor(full_path=os.path.join(BASE_PATH, LOGS_DIR_NAME, LOGS_FILE_NAME))
def average_stud (stud_list, course_name):
    x = 0
    new_list = []
    for stud in stud_list:
        if course_name in stud.courses_in_progress:
            new_list.append(course_name)
            for gr in stud.grades.values():
                for i in gr:
                    x += i
            y = x / len(gr) / len(new_list)
    print(f'Средняя оценка за домашние задания по всем студентам в рамках курса {course_name}: {y}')
    return y

@parametrized_decor(full_path=os.path.join(BASE_PATH, LOGS_DIR_NAME, LOGS_FILE_NAME))
def average_lect (lect_list, course_name):
    n = 0
    new_l = []
    for lect in lect_list:
        if course_name in lect.courses_attached:
            new_l.append(course_name)
            for g in lect.grades.values():
                for i in g:
                    n += i
            t = n / len(g) / len(new_l)
    print(f'Средняя оценка за лекции всех лекторов в рамках курса {course_name}: {t}')
    return t

print(first_reviewer)
print(first_lecturer)
print(first_student)

first_lecturer < first_student

stud_list = [first_student, second_student]
average_stud(stud_list, 'Python')

lect_list = [first_lecturer, second_lecturer]
average_lect(lect_list, 'Git')

