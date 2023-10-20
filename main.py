import requests
from bs4 import BeautifulSoup


user_year  = input('Type the year you would like to go to , Type the date in this format YYYY-MM-DD : ')



response = requests.get('https://www.billboard.com/charts/hot-100/'+user_year)

soup  = BeautifulSoup(response.text ,'html.parser')

song_names_spans = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_spans]


print(song_names)