# word = 'Abreviated'
# guessed = "_" * len(word)
# print(guessed)

# while True:
#     user_val = input("Please enter a value : ")
#     index = 0
#     for i in word:
#         if user_val == i:
#             index = word.index(i)
#             print(f"found {i} at position {index}!!!")
#             break
#     else:
#         print(f"{user_val} does not exist in {word}")

#     guessed = list(guessed)
#     guessed[index] = user_val
#     guessed = ''.join(guessed)
#     print(guessed)

# mail_list = ["john", "james", "ali"]

# for name in mail_list:
#     mesage = f"hello {name} thank you for registering today"
#     print(mesage)


# csv_file = open("mean_dev.csv", "w")

# x = 1,2,3,4,5,6,6,7,81,2,3,4,5,6
# y= 10,2,4,7,2,9,8,3,634,2,4,5,6,4
# mean_x = sum(x)/len(x)
# mean_y = sum(y)/len(y)
# x_xbar = [i - mean_x for i in x]
# y_ybar = [i - mean_y for i in y]

# print(f'{"x".center(8)}|{"y".center(8)}|{"x_xbar".center(8)}|{"y_ybar".center(8)}')
# print(f'{"x".center(8)},{"y".center(8)},{"x_xbar".center(8)},{"y_ybar".center(8)}', file = csv_file)
# print(f'{"--------".center(8)}|{"--------".center(8)}|{"--------".center(8)}|{"--------".center(8)}')

# for i in range(len(x)):
#     x_val = x[i]
#     y_val = y[i]
#     ybar_val = round(y_ybar[i], 2)
#     xbar_val = round(x_xbar[i], 2)
#     print(f'{str(x_val).center(8)}|{str(y_val).center(8)}|{str(xbar_val).center(8)}|{str(ybar_val).center(8)}')
#     print(f'{str(x_val).center(8)},{str(y_val).center(8)},{str(xbar_val).center(8)},{str(ybar_val).center(8)}', file = csv_file)

# csv_file.close()

# x = [1,2,3,4,5]

# for i in range(len(x)):
#     print(x[i], x[i-1])

# csv_file = open("mean_dev.csv", "r")

# data = csv_file.read()
# print(data)
# print(data.splitlines())

# for line in data.splitlines():
#     print(line)


##APIs AS DICTIONARY SOURCE

import requests

api_key = "336b102582e7d317c464efd5e6ac86aa"
city_id = "2332453"

url = f"http://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID={api_key}"
# url = f"http://jumia.com"
fetch = requests.get(f"{url}")
data = fetch.json()
# print(data)
# print(type(data))
# print((data.keys()))
# print(len(data))
# print(data["message"])
# print(data["cnt"])

# weather_data = data["list"]
# print(type(weather_data))
# print(len(weather_data))

# for i in weather_data:
#     print(i["dt_txt"], i["weather"][0]["description"])

# print(weather_data[0]["main"]["temp"])
# print(weather_data[1]["main"])
# print(weather_data[2]["main"])
# 
# get the date, weather and temp
def kel2cel(_temp):
    converted = int(_temp) - 273

    return converted

_list = data['list']
for response in _list:
    # print(response)
    print(f"Date : {response['dt_txt']}\nWeather: {response['weather'][0]['description']}")
    
    
    main = response['main']
    unconverted = main['temp']
    convert = kel2cel(unconverted)
    print(f"Temperature(C) : {convert}\nTemperature(F) : {main['temp']}")

    
    