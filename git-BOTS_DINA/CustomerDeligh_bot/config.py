import json 
import requests


TOKEN = '7146043359:AAF1yGNLjC1KUJWdP8_MHWjxhBQTKPdJmd8'  
URL = f'https://api.telegram.org/bot{TOKEN}'
print(requests.get(URL + '/getUpdates').json())  # сис. инфа о пользователе

