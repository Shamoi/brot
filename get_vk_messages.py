def get_message(vk, chat_id, last_message_id):
    response = vk.method('messages.getHistory', {"chat_id" : chat_id, "count" : 1})
    if response["items"][0]["id"] > last_message_id:
        return {"time" : response["items"][0]["date"], "sender" : response["items"][0]["from_id"],
                "chat-id" : response["items"][0]["chat_id"], "id" : response["items"][0]["id"],
                "text" : response["items"][0]["body"]}
    else:
        return None
