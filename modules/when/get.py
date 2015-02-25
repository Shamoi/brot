import time
import requests

def getTemperature():
    r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22Votkinsk%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
    return str(int((int(json.loads(r.text)["query"]["results"]["channel"]["item"]["condition"]["temp"]) - 32) * 5 / 9 // 1)) + " градусов цельсия"

def get(message):
    return {"text" : ["Сейчас в Воткинске " + getTemperature()], "photos" : []}
