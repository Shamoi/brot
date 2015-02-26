import time

def send_messages(messages, vk, chat_id):
    for message in messages["text"]:
        if message and (message != " "):
            response = vk.method('messages.send',
                              {"chat_id" : chat_id, "message" : message})
    try:
        for pic in messages["photos"]:
            response = vk.method('messages.send',
                                {"chat_id" : chat_id, "attachment" : pic})
    except KeyError:
        pass
    except Exception:
        pass
