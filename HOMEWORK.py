from statistics import mean

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def mean_grades(self):
        list_grades = []
        all_grades = [el for el in self.grades.values()]
        for el in range(len(all_grades)):
            list_grades += all_grades[el]
        return round(mean(list_grades), 1)


class Student(Mentor):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) 
            and course in self.courses_in_progress
            and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'\nИмя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: '
                f'{Lecturer.mean_grades(self)}\n'
                f'Курсы в процессе изучения: '
                f'{", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}') 

    def __lt__(self, other):
        if not isinstance(other, Lecturer) :
            print('Оценок нет')
        return self.Lecturer < other.Lecturer
    
    def student_average_grade(self):
        students_grade_list = []
        for s_g_l in self.grades.items():
            for i in s_g_l:
                grade_list.append(i)
        result = round(sum(grade_list) / len(grade_list), 2)
        return result       


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f'\nИмя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {Lecturer.mean_grades(self)}')
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer.mean_grades) :
            print('Оценок нет')
        return self.Lecturer.mean_grades < other.Lecturer.mean_grades
    
    def lecturer_average_grade(self):
        lecturers_grade_list = []
        for l_g_l in self.grades.items():
            for i in l_g_l:
                grade_list.append(i)
        result = round(sum(grade_list) / len(grade_list), 2)
        return result    
    

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) 
            and course in self.courses_attached
            and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"\nИмя: {self.name}\nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']


cool_reviewer.rate_hw(best_student, 'Python', 9.9)
cool_reviewer.rate_hw(best_student, 'Python', 9.8)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

lecturer = Lecturer('Some', 'Buddy')
lecturer.courses_attached += ['Python']

best_student.rate_hw(lecturer, 'Python', 9.9)
best_student.rate_hw(lecturer, 'Python', 9.9)
best_student.rate_hw(lecturer, 'Python', 10)

print(lecturer.grades)

print(cool_reviewer)

print(lecturer)

print(best_student)