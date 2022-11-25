# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from random import randint

def play():
    random_int = randint(0,100)

    while True:
        user_guess = int(input('What number did we guess (0-100)?'))

        if user_guess == random_int:
            print(f'You found the number ({random_int}). Congrats!')
            break
        if user_guess < random_int:
            print('Your number is less than the correct number')
            continue
        if user_guess > random_int:
            print('You number is more than the correct number')
            continue

if __name__ == '__main__':
    play()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
