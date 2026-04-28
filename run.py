def Addition(num1,num2):
    return num1 + num2

def Subtraction(num1,num2):
    return num1 - num2

def Multiplication(num1,num2):
    return num1 * num2

def Division(num1,num2):
    return num1 / num2

def main():
    try:
        number1 = float(input('1 Number ->'))
        number2 = float(input('2 Number ->'))
        action = input('action (+,-,*,/) ->')
        if action == '+':
            print('Result ->',Addition(number1,number2))
        if action == '-':
            print('Result ->',Subtraction(number1,number2))
        if action == '*':
            print('Result ->',Multiplication(number1,number2))
        if action == '/':
            print('Result ->',Division(number1,number2))
    except ValueError:
        print('Enter the correct number or digit!')

if __name__ == '__main__':
    while True:
        main()