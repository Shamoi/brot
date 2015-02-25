import vk_api
import wikipedia
import json
import requests
import os

config = json.loads(open('config.json').read())
vk = vk_api.VkApi(config["vk-login"], config["vk-password"])
wikipedia.set_lang("ru")

def get(message):
    response = vk.method("photos.getUploadServer", {})
    file_name, headers = urllib.request.urlretrieve(wikipedia.page(message["text"].split(" ")[2]).images[0])
    print(file_name)
    r = requests.post(response["upload_url"], files = {'photo': open(file_name, 'rb')})
    print(r.text)
    response = vk.method("photos.save", {"album_id" : 211634157, "server" : json.loads(r.text)["server"],
                                         "photos_list" : json.loads(r.text)["photos_list"], "hash" : json.loads(r.text)["hash"]})
    return {"text" : [wikipedia.summary(message["text"].split(" ")[2], sentences = 3)],
            "photos" : ["photo" + response["items"][0]["owner_id"] + "_" + response["items"][0]["id"]]}
