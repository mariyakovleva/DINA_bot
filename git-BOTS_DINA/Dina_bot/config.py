import json 
import requests


TOKEN = '7045326074:AAFpUTw3UlXW58fbQ703ikIwgdNdWT0HZyU'  
URL = f'https://api.telegram.org/bot{TOKEN}'
print(requests.get(URL + '/getUpdates').json())  # сис. инфа о пользователе

