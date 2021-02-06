while True:
    a = str(input(' -, +, *, / '))
    b = float(input('give your first number '))
    c = float(input('give your second number '))
    if a == '-':
        print(b - c)
        i = str(input('do you wanna do another calculation?(y or n) '))
        if i == 'y':
            print('please do the inputs again')
        else:
            break
    elif a == '+':
        print(b + c)
        i = str(input('do you wanna do another calculation?(y or n) '))
        if i == 'y':
            print('please do the inputs again')
        else:
            break
    elif a == '*':
        print(b * c)
        i = str(input('do you wanna do another calculation?(y or n) '))
        if i == 'y':
            print('please do the inputs again')
        else:
            break
    elif a == '/':
        print(b / c)
        i = str(input('do you wanna do another calculation?(y or n) '))
        if i == 'y':
            print('please do the inputs again')
        else:
            break