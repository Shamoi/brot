def get_message(vk, chat_id, last_message_id, ignored_users):
    try:
        response = vk.method('messages.get', {"last_message_id" : last_message_id, "count" : 1})
    except Exception as error_msg:
        print(error_msg)
        return None

    if response["items"]:
        try:
            message = {"time" : response["items"][0]["date"], "sender" : response["items"][0]["user_id"],
                       "chat_id" : response["items"][0]["chat_id"], "id" : response["items"][0]["id"],
                       "text" : response["items"][0]["body"]}
        except KeyError:
            message = {"time" : response["items"][0]["date"], "sender" : response["items"][0]["user_id"],
                       "chat_id" : "", "id" : response["items"][0]["id"], "text" : response["items"][0]["body"]}
        if response["items"][0]["user_id"] in ignored_users: #Check, if sender are ignored - ignore message
            return None
        return message
    else:
        return None
