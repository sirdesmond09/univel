# # class ElectionWinner:
# #   @staticmethod
# #   def voteWinner(votes):
# #     #Please write your code here.
# #     count = 0
# #     winner = ""
    
# #     votes.sort()

# #     for _voter in reversed(votes):
# #       if votes.count(_voter) > count:
# #         count = votes.count(_voter)
# #         winner = _voter
        

# #     return winner
# # votes_count = 4
# # votes = []

# # print(ElectionWinner.voteWinner(["Glenn","Emily","Emily","Glenn", "Ada","Ada"]))

# import random
# import curses

# s = curses.initscr()
# curses.curs_set(0)
# sh, sw = s.getmaxyx()
# w = curses.newwin(sh, sw, 0, 0)
# w.keypad(1)
# w.timeout(100)

# snk_x = sw/4
# snk_y = sh/2
# snake = [
#     [snk_y, snk_x],
#     [snk_y, snk_x-1],
#     [snk_y, snk_x-2]
# ]

# food = [sh//2, sw//2]
# w.addch(food[0], food[1], curses.ACS_PI)

# key = curses.KEY_RIGHT

# while True:
#     next_key = w.getch()
#     key = key if next_key == -1 else next_key

#     if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
#         curses.endwin()
#         quit()

#     new_head = [snake[0][0], snake[0][1]]

#     if key == curses.KEY_DOWN:
#         new_head[0] += 1
#     if key == curses.KEY_UP:
#         new_head[0] -= 1
#     if key == curses.KEY_LEFT:
#         new_head[1] -= 1
#     if key == curses.KEY_RIGHT:
#         new_head[1] += 1

#     snake.insert(0, new_head)

#     if snake[0] == food:
#         food = None
#         while food is None:
#             nf = [
#                 random.randint(1, sh-1),
#                 random.randint(1, sw-1)
#             ]
#             food = nf if nf not in snake else None
#         w.addch(food[0], food[1], curses.ACS_PI)
#     else:
#         tail = snake.pop()
#         w.addch(int(tail[0]), int(tail[1]), ' ')

#     w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)


# x = 20
# y = 30

# answer = x + y

# print(answer)

# num = 20
# den = 60
# pi = den / num
# print(pi)

# nameTe = "Hammed"
# print(nameTe)

# phone = 8023900964 * 2

# print(phone)

# firstName = "Hammed"
# surname = "Balogun"
# fullname = firstName + ' ' + surname

# print(fullname)
# day = "10"
# month = "06"
# year = "1988"
# print(day + ' / ' + month + ' / ' + year )
# pi = 22 / 7
# statement = "pi is " + str(round(pi,2))
# print(statement)

# akara = input("Please how many akara do you want: ")
# akamu = input("Please how many akamu do you want: ")

# akaraPrice = 20
# akamuPrice = 50

# cost1 = akaraPrice * int(akara)

# cost2 = akamuPrice * int(akamu)

# total = cost1 + cost2

# print("You bill is: ", "#",total)

# name = input("Please enter your name: ")
# age = input("Please enter your age: ")

# currentAge = 2019 - int(age)

# answer = f"Hello {name} you are {age}, you were born in {currentAge}"

# print(answer)

# word  = input("Please enter word : ")
# length  = input("Please enter word length : ")
 
# half_length = int(int(length)/2) - 1
# two_chars_up = half_length + 2

# first_two = word[0:2]
# last_two = word[-2:]
# mid_point = word[half_length : two_chars_up]

# # statement = f"{first_two}{mid_point}{last_two}"
# statement = first_two + mid_point + last_two

# print(statement)
# # print(word[half_length : two_chars_up])


# age = int(input("Please enter your age : "))

# can_drink = age >= 20
# can_pay_tax = age >= 18
# can_take_pension = age > 60
# can_retire = age == 40

# statement = f"Can drink : {can_drink}\nCan Pay Tax : {can_pay_tax}\nCan take pension : {can_take_pension}\nCan now retire : {can_retire}"

# print(statement)

# word = input('Please enter word : ')
# reversed_word = word[::-1]
# print(f"{word} is a palindrome : {word ==reversed_word}")

# response  = 'a' in word or 'e' in word or 'i' in word or 'u' in word
# print(f"{word} contains vowels : {response}")

# fraction = input("Please enter a fraction in the format 'a/b+c/d' : ")
# splitted_fraction = fraction.split("+")
# frac1 = splitted_fraction[0]
# frac2 = splitted_fraction[1]

# splitted_frac1 = frac1.split('/')
# splitted_frac2 = frac2.split('/')

# a = splitted_frac1[0]
# b = splitted_frac1[1]
# c = splitted_frac2[0]
# d = splitted_frac2[1]

# # print(fraction)
# # print(splitted_fraction)
# # print(splitted_frac1)
# # print(splitted_frac2)
# # print(a,b,c,d)

# frac1, frac2 = fraction.split("+")

# a, b, c, d = *frac1.split('/'), *frac2.split('/')

# print(a,b,c,d)

# filename = "lyrics (2).txt"
# mode = "r" #read mode open
# data = open(filename, mode)

# lyrics  = data.read()
# print(lyrics)
# filename = "file.csv"
# mode = "w" #read mode open
# file = open(filename, mode)

# text = "Atha, science, eating"
# file.write(text)


import requests
import datetime

response = requests.get("http://checklight.pythonanywhere.com/get_readings/1x0d001/12/")

data = response.json()["streets"]
previous_time = 0
previous_status = 0
status_ones = []

days = {}

for post in data:

    time = post['time']
    conv_time =  datetime.datetime.strptime(time, "%b. %d,  %Y, %I:%M %p.")

    if previous_time == 0:
        previous_time = conv_time
        previous_status = post["status"]
        continue
    
    time_diff = conv_time - previous_time
    previous_time = conv_time

    if previous_status == 1 and post["status"] == 1:
        if conv_time.day not in list(days.keys()):
            # print(days.keys())
            # print(conv_time.day, time_diff)
            days[conv_time.day] = []

        days[conv_time.day].append(time_diff.seconds)

        status_ones.append(time_diff.seconds)

    previous_status = post["status"]

for key in days:
    days[key] = sum(days[key])

print(sum(status_ones), "seconds")
print(sum(status_ones)/(60), "minutes")
print(sum(status_ones)/(60*60), "hours")
print(sum(status_ones)/(60*60*24), "days")
print(days)

    # print(conv_time)