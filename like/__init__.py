from vk_functions import fast_send_message, vk_method

def get(message):
    fast_send_message(message=message, text='Сейчас лайкну')
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
