
def calculator():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    opp = input("Enter operation (+, -, *, /): ")
    if opp == '+':
        print(x + y)
    elif opp == '-':
        print(x - y)
    elif opp == '*':
        print(x * y)
    elif opp == '/':
        print(x / y)
    else:
        print("Sorry that is not an operation! ")


type = input('Do you want to know a question with the 4 basic operations? ')
if type == 'yes':
    calculator()
otype = input('Do you want to use percentages, exponents or roots? ')
if otype == 'roots':
    n = int(input('what type of root do you want? (put in your answer as a numeral like 3 for cube roots ) '))
    x = int(input('what is the number you will be puting in your root? '))
    print(x**(1 / n))
if otype == 'percentages':
    x = input('what number do you want to find a percentage of? ')
    n = input('what percentage of the number do you want ')
    print((int(n) / 100) * int(x))
if otype == 'exponents':
    x = input('what number are we using exponents on? ')
    y = input('what numeral exponent are we using? ')
    print(pow(int(x), int(y)))

    



    

