'''
PROBLEMS STATEMENT:
The problem statement is a bit complex so I am just adding the link to the solution

Here:
https://www.hackerrank.com/challenges/grading/problem
'''


import numpy as np

n = input()

def create_grades(n):
    grades = []
    for i in range(int(n)):
        grade = input()
        grades.append(grade)

    return grades

student = create_grades(n)

def curve_grades(student):
    curved =[]
    for j in range(len(student)):

        grd = int(student[j])

        if grd%5 != 0:
            mult  = np.round((np.floor(grd/5)+1)*5)
            check = mult-grd
            if check < 3:
                curv_grd = mult
                curved.append(curv_grd)
            else:
                curved.append(grd)

        elif grd < 38:
                curv_grd = grd
                curved.append(curv_grd)
        else:
            curved.append(grd)
    return curved

graded_students = curve_grades(student)
print ('\n')
for k in graded_students:
    print(k)
