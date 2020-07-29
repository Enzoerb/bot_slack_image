from slack_info import TOKEN, WEBHOOOK
from datetime import datetime
import requests
import json
from sys import argv
from os import path

if len(argv) > 1:
    paths = argv[1:]
else:
    paths = ['/home/semantix/Documentos/Desafios/svg_coronavirus(p6)/svg_data/corona_brazil.png']

date_data = {'text': f'{datetime.now()}'}
requests.post(WEBHOOOK, data=json.dumps(date_data))

for image_location in paths:

    filename = path.basename(image_location)

    with open(f'{image_location}', 'rb') as image:

        param = { "filename": filename,
                  "token": TOKEN,
                  "channels": "graficos-coronavirus" }

        files = dict()
        files['file'] = image

        requests.post("https://slack.com/api/files.upload", params=param, files=files)
