import requests
import datetime

url = 'http://checklight.pythonanywhere.com/get_readings/1x0d001/7/'

response = requests.get(url)

data = response.json()                                                                                      

# print((data['sreets'][0]['status']))
# street = data['streets']
# print(len(street))

# ones  = []
# zeros = []
# _t1 = []                 
# for i in range(len(street)):

#     status_list = street[i]
    
#     if status_list['status'] == 1:
#         # ones.append(status_list['status'])
#         time = status_list['time']
#         converts = datetime.datetime.strptime(time, "%b. %d, %Y, %I:%M %p.")
#         _t1.append(converts)
#         num = 0
#         for i in range(len(_t1)):
#             if i == len(_t1)-1:
#                 break

#             first = _t1[num]
#             interval = _t1[i + 1] - first
#             num+=1
#             print (interval)
            
 
            
    # elif status_list['status'] == 0:
    #     zeros.append(status_list['status'])

# print(f"Total number of 1 occurences is:\n{len(ones)}")
# print(f"Total number of 0 occurences is:\n{len(zeros)}")

# time = "Nov. 12, 2019, 08:33AM"
# convertedtime = datetime.datetime.strptime(time, "%b. %d, %Y, %I:%M%p")
# print(convertedtime)

# timet = "Nov. 12, 2019, 09:52AM"
# convert = datetime.datetime.strptime(timet, "%b. %d, %Y, %I:%M%p")
# print(convert)

# duration = convert - convertedtime
# print(duration)


datas = data['streets']
previous_time = 0
previous_status = 0
status_ones = []

days = {}

for post in datas:

    time = post["time"]
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

import matplotlib.pyplot as plt
days_num = []
hours = []
for key in days:
    days_num.append(key)
    hours.append(days[key])

plt.barh(days_num, hours)
plt.show()

