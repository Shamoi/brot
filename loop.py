import vk_api

import get_vk_messages
import out_vk_messages
import parse_messages

#vk = VKontakte object
#last-message-id = Last message ID, which taken from VK object

def start_loop():
    while True: #Infinity loop
        message = get_vk_messages.get_message() #(VK object)
        out_vk_messages.send_messages(parse_messages.parse(message))
