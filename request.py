# import requests

# url = 'http://checklight.pythonanywhere.com/predictions/1x0d001/'

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

# url2 = "http://jumia.com"

# def makerequest(url):
#     response = requests.get(url)
#     data = response.content()
#     return data


# response = makerequest(url)
# print(response)

# response2 = makerequest(url2)
# print(response2)

# print(f"status {response.text}")


###Using Requests to get Images

# import requests
# from io import BytesIO
# from PIL import Image

# img_data = requests.get("https://digitalart.io/storage/artworks/1148/world-of-warcraft-wallpaper.jpeg")

# print(f"Status: {img_data.status_code}")

# image = Image.open(BytesIO(img_data.content))
# print(image.size, image.format, image.mode)

# path = f"image.{image.format.lower()}"

# try:
#     image.save(path, image.format)
# except IOError:
#     print("cannot save image")

###Posting with Requests
import requests

mydata = {"name" :"Nick", "email" : "email@email.com"}
response = requests.post("https://www.w3schools.com/php/welcome.php", data= mydata)
