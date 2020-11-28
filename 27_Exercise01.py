"""
Write a program with an infinite loop and a list of numbers.
Each time through the loop the program should ask the user
to guess a number (or type q to quit).If they type q,
the program should end. Otherwise,it should tell them
whether or not they successfully guessed a number in the list or not.
"""
numbers = [11, 32, 33, 15, 1]
while True:
    answer = input("Guess a number or type q to quit.")
    if answer == 'q':
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly")