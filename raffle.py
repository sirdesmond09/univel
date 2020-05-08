import random
import time

draws =int(input("How many do you want to draw\n\n> "))

move = 0



chosen = []

numbers = [12, 23, 42, 223, 22, 1321, 40]

for i in range(draws):
    choice = random.choice(numbers)
    chosen.append(choice)
    numbers.remove(choice)


    print('\n\n', choice)
    print('\n\n', chosen)
    print('\n\n', numbers)
    time.sleep(2.5)

    