from vk_api import VkApi
from config import VK_LOGIN, VK_PASSWORD

vk = VkApi(login=VK_LOGIN, password=VK_PASSWORD)  # Authorization in VK


def get_message(last_message_id=0, specify_dialog=False,
                specify_dialog_type=None, id=None):
    """ Получение сообщения из ВКонтакте


    :param last_message_id: id последнего обработанного сообщения
    :param specify_dialog: получать сообщение из конкретного диалога
    :param specify_dialog_type: тип конкретного диалога (chat/user)
    :param id: id конкретного диалога, если параметр type равен True
    :return: словарь с данными о сообщении
    """

    if specify_dialog and specify_dialog_type and id:
        values = {
            'count': 1,
            'start_message_id': last_message_id
        }
        if specify_dialog_type == 'chat':
            values.update({'chat_id': id})
        elif specify_dialog_type == 'user':
            values.update({'user_id': id})
        else:
            print("Передан неправильный specify_dialog_type")
        response = vk_method('messages.getHistory', values)
    else:
        values = {
            'count': 1,
            'last_message_id': last_message_id
        }
        response = vk_method('messages.get', values)

    if response["items"]:
        loaded_message = response["items"][0]
        loaded_attachments = []
        if "attachments" in loaded_message:
            for attachment in loaded_message['attachments']:
                type_of_attachment = attachment['type']
                loaded_attachments.append('{type}{owner}_{id}'.format(
                    type=type_of_attachment,
                    owner=attachment[type_of_attachment]['owner_id'],
                    id=attachment[type_of_attachment]['id']
                ))

        message = {
            'id': loaded_message['id'],
            'sender_id': loaded_message['user_id'],
            'type': 'chat' if 'chat_id' in loaded_message else 'dialog',
            'chat': loaded_message['chat_id'] if 'chat_id' in loaded_message else None,
            'body': loaded_message['body'],
            'attachments': loaded_attachments
        }
        return message
    else:
        return None



def send_message(message='Произошла ошибка. Код ошибки: 02.2.0',
                 attachments=None):
    """ Отправляет сообщение и вложения к нему


    :param message: текст сообщения
    :param attachments: список вложений
    :return: результат отправки сообщения
    """
    return True


def vk_method(method, values):
    """ Использование метода ВКонтакте


    :param method: необходимый метод
    :param values: параметры для метода
    :return: ответ ВКонтакте на запрос
    """
    response = vk.method(method, values)
    return response