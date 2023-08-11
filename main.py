from requests import *
from telegram import *
from telegram.ext import *

TOKEN = '6413837352:AAEsxbSeeOd36NB1PdFYvdtX3u3hSXEZ2xA'

RANDOM_IMAGE = 'Random image'
GET_MP3 = 'Get mp3'
RANDOM_IMG_URL = "https://picsum.photos/1200"


global IMAGE_COUNTER
IMAGE_COUNTER = 0

print('Running up the bot...')
