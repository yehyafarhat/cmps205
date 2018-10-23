max = 1000
min = 1
number = int(input('please think of a number between {0} and {1}:'.format(min,max)))
while True:
    guess = ((min+max)//2)
    print('is your number {0}?'.format(guess))
    answer = str(input("enter 'yes' to i guessed correctly\n"
                        "enter 'false to its more than the number above\n"
                        "enter 'true' to its less than the number above\n"))
    if answer == 'false':
        min = guess
    elif answer == 'true':
        max = guess
    elif answer == 'yes':
        print('your number is ' + str(guess))
        break