import requests
import xml.etree.ElementTree as ET

from consts import *

def current_song():
    
    # Возвращает имя артиста и название трека, который играет на данный момент

    data = ET.fromstring(requests.get(f"{RADIOBOSS_SERVER}/?pass={RADIOBOSS_PASSWORD}&action=playbackinfo").content.decode('utf-8')[1:-2])
    output = data.findall('.//TRACK')[1].attrib['ARTIST'] + ' - ' + data.findall('.//TRACK')[1].attrib['TITLE']
    return output

def current_listeners():

    # Возвращает текущее количество слушателей
    
    data = ET.fromstring(requests.get(f"{RADIOBOSS_SERVER}/?pass={RADIOBOSS_PASSWORD}&action=playbackinfo").content.decode('utf-8')[1:-2])
    amount = data.findall('./Streaming')[0].attrib['listeners']
    return amount

def next():

    # Переключает трек на следующий

    return requests.get(f"http://{RADIOBOSS_SERVER}/?pass={RADIOBOSS_PASSWORD}&cmd=next").content.decode("utf-8")

