import vk_api

from get_vk_messages import get-message
from parse_messages.py import parse
#vk = VKontakte object
#last-message-id = Last message ID, what taken from VK object

def start-loop():
    while True: #Infinity loop
        get-message() #(VK object)
