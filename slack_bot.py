from slack_info import TOKEN
import requests
import json
from sys import argv
from os import path

if len(argv) > 1:
    image_location = argv[1]
else:
    image_location = '/home/semantix/Documentos/Desafios/svg_coronavirus(p6)/svg_data/corona_us.svg'

filename = path.basename(image_location)

with open(f'{image_location}', 'rb') as image:

    param = { "filename": filename,
              "token": TOKEN,
              "channels": "graficos-coronavirus" }

    files = dict()
    files['file'] = image

    requests.post("https://slack.com/api/files.upload", params=param, files=files)
