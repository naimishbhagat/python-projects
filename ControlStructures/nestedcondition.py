a=10
b=20

if a>5:
    print('A is greater than 5')
    if b>15:
        print('B is greater than 15')
    else:
        print('B is less than 15')
else:
    print('A is Less than 5')

age = int(input('Enter your age: '))

if age>=18:
    score = int(input('Enter your exam score'))
    if score>=40:
        print('You meet both the age and score criteria, you are qualified')
    else:
        print('You meet both the age criteria but do not meet score criteria')
else:
    print('You do not meet the age criteria, please try when you are above 18')