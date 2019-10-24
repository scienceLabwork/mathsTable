x = 'Y'
while x=='Y':
    numberOf = input('TABLE OF WHICH NUMBER? ')
    if numberOf.isdigit()==True:
        for x in range(0,11):
            y = (int(numberOf) * x)
            print(numberOf,'x',x,'=',y)
    else:
        print('Please input a Number')
    x = input('Want to get table of another number(Y/n) ')
    
print('Tables calculator by Rudra shah')
