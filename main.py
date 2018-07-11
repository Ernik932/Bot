import time, json
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# Чтение токена из файла
file_secret = open("secret.json", 'r')
json_secret = json.load(file_secret)
TOKEN = json_secret["token"]

vk = vk_api.VkApi(token = TOKEN) # Авторизоваться как сообщество
longpoll = VkLongPoll(vk)

values = {'out': 0,'count': 100,'time_offset': 60}

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})

for event in longpoll.listen():
    if (event.type == VkEventType.MESSAGE_NEW) and (event.to_me):
        user_id = event.user_id
        user_text = event.text.lower().strip()
        print(user_id, user_text)
        vk.get_api().messages.send(user_id=user_id, message="Ваше сообщение: %s" % user_text)
