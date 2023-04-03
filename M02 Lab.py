'''
Molly Monroe
M02 Lab.py
This app will
'''
last_name = input("What is your last name? (or ZZZ to quit)")
if last_name == 'ZZZ':
    quit()
first_name = input("What is your first name?")
student_gpa = float(input("What is your current GPA?"))
if student_gpa > 3.5:
    print('You have made the deans list!')
elif student_gpa > 3.25:
    print('You have made honor roll!')