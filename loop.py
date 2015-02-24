import vk_api

import get_vk_messages
import out_vk_messages
import parse_messages

import time
import json


def start_loop():

    config = json.loads(open('config.json').read())
    vk = vk_api.VkApi(config["vk-login"], config["vk-password"])
    chat_id = config["chat-id"]
    response = vk.method('messages.getHistory', {"chat_id" : chat_id, "count" : 1}) #Take id of last message
    last_message_id = response["items"][0]["id"]

    while True: #Infinity loop
        message = get_vk_messages.get_message(vk, chat_id, last_message_id) #(VK object)
        if message:
            answer = parse_messages.parse(message)
            if answer:
                out_vk_messages.send_messages(answer)
            last_message_id = message["id"]
    time.sleep(0.5)
