from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/newest"

request = requests.get(url)

soup = BeautifulSoup(request.text, "html.parser")

teme = soup.find_all("td", class_="title")

for temes in teme:
    
    temes = temes.find("a", {'class':'storylink'})
