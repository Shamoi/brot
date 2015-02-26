import time

def send_messages(messages, vk, chat_id, message_q):

    for message in messages["text"]:
        if message and (message != " "):
            try:
                if message_q["chat_id"]:
                    response = vk.method('messages.send',
                                    {"chat_id" : message_q["chat_id"], "message" : message})
                else:
                    response = vk.method('messages.send',
                                     {"user_id" : message_q["sender"], "message" : message})
            except Exception:
                return 0
    try:
        for pic in messages["photos"]:
            if message_q["chat_id"]:
                response = vk.method('messages.send',
                                    {"chat_id" : message_q["chat_id"], "attachment" : pic})
            else:
                response = vk.method('messages.send',
                                    {"user_id" : message_q["sender"], "attachment" : pic})
    except KeyError:
        pass
    except Exception:
        pass
