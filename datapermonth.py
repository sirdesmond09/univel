import requests
import datetime 

url = 'http://checklight.pythonanywhere.com/get_readings/1x0d001/30/'

response = requests.get(url)

data = response.json()['streets']

days = {}
one  = []
zero = []
on_time  = []
off_time = []
previous_time = 0
# print(data['time'])

for posts in data:
    if previous_time == 0:
        time = posts['time']
        converted_time = datetime.datetime.strptime(time, "%b. %d, %Y, %I:%M %p.")
        previous_time = converted_time
        previous_status = posts["status"]
        continue

    total_time = converted_time + previous_time
    previous_time = converted_time

    if posts['status'] == 1:
        if converted_time.day not in list(days.keys()):
            days[converted_time.day] = []
            days[converted_time.day].append(total_time.seconds)

    # else:
    #     zero.append(posts['status'])
    #     time = posts['time']
    #     converted_time = datetime.datetime.strptime(time, "%b. %d, %Y, %I:%M %p.")
    #     off_time.append(converted_time)

# print(on_time, '\n\n\n')
# print(off_time)

print(days)