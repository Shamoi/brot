from vk_functions import send_message, vk_method

def get(message):
    send_message(
        message='Сейчас лайкну',
        attachments=[],
        type=message['type'],
        send_to=message['sender_id'] if message['type'] == 'user'
                else message['chat']
    )
    response = vk_method('users.get', {
        'user_ids': message['sender_id'],
        'fields': 'photo_id'
    })
    vk_method('likes.add', {
        'type': 'photo',
        'owner_id': message['sender_id'],
        'item_id': int(response[0]['photo_id'].split('_')[1])
    })
    return {'text': 'Готово', 'attachments': []}
