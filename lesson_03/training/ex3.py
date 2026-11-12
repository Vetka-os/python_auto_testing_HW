from student import Student
from course_group import CourseGroup

course_group = CourseGroup(
    Student("Петя", "Васечкин", 18, 1),
    classmates=[
        Student("Вася", "Петров", 19, 1),
        Student("Наташа", "Олеговна", 18, 1),
        Student("Егор", "Фазанов", 20, 1),
        Student("Анна", "Леонидовна", 30, 1),
    ],
)


names = ", ".join(
    [f"{c.first_name} {c.last_name}, {c.age} лет" for c in course_group.classmates]
)

print(
    f"{course_group.student.first_name} {course_group.student.last_name}, {course_group.student.age} лет, учится на курсе {course_group.student.course} вместе с: {names}"
)
