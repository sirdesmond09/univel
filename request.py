import requests

url = 'http://checklight.pythonanywhere.com/predictions/1x0d001/'

# response = requests.get(url)

# print(response)

# data = response.json()

# # print(data)
# print(type(data))
# print(data.keys())
# print(data['day'])
# predictions = (data['predictions'])
# print(type(predictions))

# for data_point in predictions:
#     # print (data_point)
#     print(f"Hour : {data_point['hour']}, Prediction : {data_point['prediction']}, Confidence : {data_point['confidence']}")

# url = "http://jumia.com"

# response = requests.get(url)

# print(response.content)

url2 = "http://jumia.com"

def makerequest(url):
    response = requests.get(url)
    data = response.content()
    return data


response = makerequest(url)
print(response)

response2 = makerequest(url2)
print(response2)