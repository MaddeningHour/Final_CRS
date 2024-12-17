from random import *

def question1():
    total = 12.8 + 18.2 + 0.4
    print(f'The answer to question 1 is:\n{total:.2f}')


def question2():
    print('\nThe answer to question 2 is:')
    while True:
        try:
            myFloat = float(input('Enter your float: '))
            print(f'{myFloat:.2f}, {type(myFloat)}')
            break

        except ValueError:
            print('ERROR! Input must be of type float.')

    
def question3():
    print('\nThe answer to question 3 is:')
    radius = 3.5
    PI = 3.14159
    diameter = radius * 2
    circumference = 2 * PI * radius
    area = PI * (radius ** 2)
    print(f'Radius: {radius}\nDiamter: {diameter:.2f}\nCircumference: {circumference:.2f}\nArea: {area:.2f}')


def question4():
    print('\nThe answer to question 4 is:')
    print(f'{"number":>10}{"square":>10}{"cube":>10}')
    for i in range(0,6):
        print(f'{(i):>10} {(i**2):>9} {(i**3):>9}')


def question5():
    print('\nThe answer to question 5 is:')
    y = 0
    z = 0
    while True:
        try:     
            x = int(input('Enter an integer: '))
            
            if x > 100:
                y = 20
                z = 40
            print(f'X = {x}, Y = {y}, Z = {z}')
            break

        except ValueError:
            print('ERROR! Input must be of type integer')

    
def question6():
    print(f'\nThe answer to question 6 is:')
    myGrades = [98,76,71,87,83,90,57,79,82,94]
    average = (sum(myGrades)/len(myGrades))
    print(f'The average of all the students grades is {average:.2f}')


def question7():
    print('\nThe answer to question 7 is:')
    for i in range(33,-1, -3):
        print(f'{i}')


def question8():
    print('\nThe answer to question 8 is:')
    while True:
        try:
            myInt = int(input('Enter an integer: '))
            print(f'{myInt} squared is {myInt**2}')
            return myInt
        except ValueError:
            print('ERROR! Input must be of type integer.')


def question9():
    print('\nThe answer to question 9 is:')

    for i in range(1,11):
        myRoll = randint(0,6)
        print(f'Roll {i}: {myRoll}')


def question10():
    print('\nThe answer to question 10 is:')
    list1 = [10,20,30]
    list2 = [40,50]
    concatenated_list = list1 + list2
    print(f'Your concatenated list is {concatenated_list}')


def question11():
    print('\nThe answer to question 11 is:')
    x = 'ABC'
    x = list(x)
    x = "#".join(x)
    print(f'{x}')


def question12():
    print('\nThe answer to question 12 is:')
    country_codes = {'Finland': 'fi', 'South Africa' : 'za', 'Nepal' : 'np'}
    for key in country_codes.keys():
        print(key)
   

def question13():
    print('\nThe answer to question 13 is:')
    myInt = 66
    print(f'Character with ASCII value {myInt}: {chr(myInt)}')


def question14():
    print('\nThe answer to question 14 is:')
    with open("accounts.txt", 'w') as myFile:
        myFile.write('100 Bill 12.34\n200 Joe 0.00\n300 Tom 4.21')
    
    with open("accounts.txt", 'r') as myFile:
        for line in myFile:
            print(f'{line}')


        
        
        
    





question1()
question2()
question3()
question4()
question5()
question6()
question7()
question8()
question9()
question10()
question11()
question12()
question13()
question14()


class Car():
    def __init__(self, year = 2000, cylinders = 4):
        self.__year = year
        self.__cylinders = cylinders
    
    def set_year(self, year):
        self.__year = year
    def set_cylinders(self, cylinders):
        self.__cylinders = cylinders
    
    def get_year(self):
        return self.__year
    def get_cylinders(self):
        return self.__cylinders
    
    def start_engine(self):
        return('Start your engine')
    
    def __str__(self):
        return f'Your car is a {self.get_year()} model with {self.get_cylinders()} cylinders.\n{self.start_engine()}'

print('\nThe answer to the extra credit question is:')
myCar = Car(2020, 4)

print(myCar)
