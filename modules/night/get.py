import vk_api
import random
import json

config = json.loads(open('config.json').read())
vk = vk_api.VkApi(config["vk-login"], config["vk-password"])

def get(message):
    random_num = random.randint(1, 100)
    response = vk.method('wall.get', {"domain" : "dark_side_madness", "offset" : random_num})
    return {"text" : ["Случайный пост из Тьмы"], "photos" : ["wall" + str(response["items"][0]["owner_id"]) + "_" + str(response["items"][0]["id"])]}
