def send_messages(messages, vk, chat_id):
    for message in messages["text"]:
        response = vk.method('messages.send',
                              {"chat_id" : chat_id, "message" : message})
        time.sleep(0.5)
    try:
        for pic in messages["photo"]:
            response = vk.method('messages.send',
                                {"chat_id" : chat_id, "attachment" : pic})
    except KeyError:
        pass
