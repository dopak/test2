import vk_api
import requests
import datetime
from vk_bot import VkBot

vk_session = vk_api.VkApi(token=f3caee452f620cabce7d7cd684195e431c6463557dab3b284572ac4aface7331a6d7b049fe78dba961737)
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
        
            print('New message:')
            print(f'For me by: {event.user_id}', end='')
            
            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))
            
            print('Text: ', event.text)

class VkBot:

    def __init__(self, user_id):
    
        print("Создан объект бота!")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        
        self._COMMANDS = ["ПРИВЕТ", "ПОГОДА", "ВРЕМЯ", "ПОКА"]
    def _get_user_name_from_vk_id(self, user_id):
    request = requests.get("https://vk.com/id"+str(user_id))
    bs = bs4.BeautifulSoup(request.text, "html.parser")
    
    user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
    
    return user_name.split()[0]
def new_message(self, message):

    # Привет
    if message.upper() == self._COMMANDS[0]:
        return f"Привет-привет, {self._USERNAME}!"
    
    # Погода
    elif message.upper() == self._COMMANDS[1]:
        return self._get_weather()
    
    # Время
    elif message.upper() == self._COMMANDS[2]:
        return self._get_time()
    
    # Пока
    elif message.upper() == self._COMMANDS[3]:
        return f"Пока-пока, {self._USERNAME}!"
    
    else:
        return "Не понимаю о чем вы..."