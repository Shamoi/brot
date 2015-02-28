def get_message(vk, chat_id, last_message_id, ignored_users):
    try:
        response = vk.method('messages.get', {"last_message_id" : last_message_id, "count" : 1})
    except Exception as error_msg:
        print(error_msg)
        return None

    if response["items"]:
        if "chat_id" in response["items"][0]:
            message = {"time" : response["items"][0]["date"], "sender" : response["items"][0]["user_id"],
                       "chat_id" : response["items"][0]["chat_id"], "id" : response["items"][0]["id"],
                       "text" : response["items"][0]["body"]}
        else:
            message = {"time" : response["items"][0]["date"], "sender" : response["items"][0]["user_id"],
                       "chat_id" : "", "id" : response["items"][0]["id"], "text" : response["items"][0]["body"]}


        if "attachments" in response["items"][0]:
            if "photo" in response["items"][0]["attachments"][0]:
                message.update({"attachment" : "photo" + str(response["items"][0]["attachments"][0]["photo"]["owner_id"]) + "_"
                                + str(response["items"][0]["attachments"][0]["photo"]["id"])})
            elif "audio" in response["items"][0]["attachments"][0]:
                message.update({"attachment" : "audio" + str(response["items"][0]["attachments"][0]["audio"]["owner_id"]) + "_"
                                + str(response["items"][0]["attachments"][0]["audio"]["id"])})
            elif "video" in response["items"][0]["attachments"][0]:
                message.update({"attachment" : "audio" + str(response["items"][0]["attachments"][0]["video"]["owner_id"]) + "_"
                                + str(response["items"][0]["attachments"][0]["video"]["id"])})

        if response["items"][0]["user_id"] in ignored_users: #Check, if sender are ignored - ignore message
            return None


        return message
    else:
        return None
