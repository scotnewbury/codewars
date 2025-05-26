'''
Grade book
Complete the function so that it finds the average of the three scores passed
to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100.
Theres is no need to check for negative values or values greater than 100.
'''


def get_grade(s1, s2, s3):
    average_score = (s1 + s2 + s3) / 3
    if 90 <= average_score <= 100:
        return "A"
    elif 80 <= average_score < 90:
        return "B"
    elif 70 <= average_score < 80:
        return "C"
    elif 60 <= average_score < 70:
        return "D"
    else:
        return "F"


print(get_grade(95, 90, 93))
print(get_grade(85, 80, 83))
print(get_grade(75, 70, 93))
print(get_grade(65, 60, 83))
print(get_grade(55, 50, 53))
