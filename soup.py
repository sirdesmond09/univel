from bs4 import BeautifulSoup
import requests
from io import BytesIO
from PIL import Image

# search = input("Enter search Term\n>")
# params = {"q": search}
# response = requests.get("https://www.bing.com/search", params= params)

# soup = BeautifulSoup(response.text, features="lxml")

# # print(soup.prettify())
# results = soup.find("ol", {"id":"b_results"})
# links   = results.findAll("li", {"class":"b_algo"})

# for data in links:
#     data_text = data.find("a").text
#     data_ref  = data.find("a").attrs["href"]

#     if data_text and data_ref:
#         print(data_text)
#         print(data_ref)


###Working with images###
search   = input("search for: ")
params   = {"q" : search}
url      = "https://www.bing.com/images/search"
response = requests.get(url, params= params)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.findAll("a", {"class" : "thumb"})

for item in links:
    print(f"Getting {item.attrs['href']}")
    img_data = requests.get(item.attrs["href"])
    img_title = item.attrs["href"].split('/')[-1]
    img       = Image.open(BytesIO(img_data.content))
    
    path = f"./img/{img_title}"
    img.save(path, img.format)
    