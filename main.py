import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import datetime
import requests
import urllib.request
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
import yaml

#vk.messages.send(peer_id=event.object.peer_id, random_id=0, attachment=attachment)


table = {
    0 : {
        0 : """ 
        2 пара (11:15 - 12:50)
        Мат. логика пр. (369а)
        
        3 пара (13:35 - 15:10)
        Яз. програм. лек. (370лк)
        
        4 пара (15:20 - 16:55)
        1 - Яз. програм. (383)
        2 - Экология (501)
        """,
        1 : """
        1 пара (9:30 - 11:05)
        1 - Мат. логика (369а)
        2 - Физика (520)
        
        2 пара (11:15 - 12:50)
        Рус. яз. пр. (331)
        
        3 пара (13:35 - 15:10)
        Мат. анализ пр. (350)
        
        4 пара (15:20 - 16:55)
        Физ-ра
        """,
        2 : """
        2 пара (11:15 - 12:50)
        1 - Экология (302)
        2 - Яз. програм. (383лк)
        
        3 пара (13:35 - 15:10)
        Мат. анализ лек.(528)
        """,
        3 : """
        1 пара (9:30 - 11:05)
        Философия лек. (434)
        
        2 пара (11:15 - 12:50)
        Политология (324)
        
        3 пара (13:35 - 15:10)
        Физика лек. (522)
        
        4 пара (15:20 - 16:55)
        Фиизка (522)
        """,
        4 : """
        1 пара (9:30 - 11:05)
        Уч. практика лек.(434)
        
        2 пара (11:15 - 12:50)
        Мат. логика лек. (472лк)
        
        3 пара (13:35 - 15:10)
        Ин. яз.
        
        4 пара (15:20 - 16:55)
        Физ-ра
        """,
        5 : """
        2 пара (11:15 - 12:50)
        Основы ИБ л.р. (172)
        """,
        6 : """
        Нет занятий.
        """,
        },
    1 : {
        0 : """ 
        1 пара (9:30 - 11:05)
        Экология лек. (501)

        2 пара (11:15 - 12:50)
        Мат.логика пр. (369а)

        3 пара (13:35 - 15:10)
        Яз. програм. лек (370лк)

        4 пара (15:20 - 16:55)
        Яз. програм. (383)
        """,
        1 : """
        1 пара (9:30 - 11:05)
        1 - Физика (520)
        2 - Мат. логика(369а)

        2 пара (11:15 - 12:50)
        Рус. яз. лек. (331)

        3 пара (13:35 - 15:10)
        Мат. анализ пр. (350)

        4 пара (15:20 - 16:55)
        Физ-ра
        """,
        2 : """
        2 пара (11:15 - 12:50)
        1 - Экология (302)
        2 - Яз. програм. (383лк)

        3 пара (13:35 - 15:10)
        Мат. анализ лек. (528)
        """,
        3 : """
        2 пара (11:15 - 12:50)
        Философия (308)

        3 пара (13:35 - 15:10)
        Физика лек. (522)
        """,
        4 : """
        1 пара (9:30 - 11:05)
        Политология лек. (434)

        2 пара (11:15 - 12:50)
        Мат. логика лек. (472лк)

        3 пара (13:35 - 15:10)
        Ин. яз.

        4 пара (15:20 - 16:55)
        Физ-ра
        """,
        5 : """
        2 пара (11:15 - 12:50)
        Основы ИБ лек. (172)
        """,
        6 : """
        Нет занятий.
        """,
        },
    }

week = {0 : 'Знаменатель (четная неделя)', 1 : 'Числитель (нечетная неделя)'}
#message = table[datetime.datetime.today().isocalendar()[1] % 2][datetime.datetime.today().weekday()]

def main():
    vk_session = vk_api.VkApi(token='16dd4a0a9d88579ab8cf611a3ee69029f76f4034f0f67248799bdcfc203c43467a968b367d3de39b860db')
    vk = vk_session.get_api()
    vk_upl = vk_api.VkUpload(vk)
    while True:
        try:
            longpoll = VkBotLongPoll(vk_session, '202763223')
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    with open("config.yaml") as file:
                         cfg = yaml.load(file, Loader=yaml.FullLoader)
                    if cfg['mention'] == 0:
                        appeal = ''
                    else:
                        user_id = event.object.message['from_id']
                        first_name = vk.users.get(user_ids = (user_id))[0]['first_name']
                        appeal = '[id%i|%s]' % (user_id, first_name)
                    if event.object.message['text'].lower() == 'отключить упоминания' or event.object.message['text'].lower() == 'mention off':
                        if event.object.message['from_id'] == 597776932:
                            #изменение конфига
                            with open("config.yaml") as file:
                                 cfg = yaml.load(file, Loader=yaml.FullLoader)
                            cfg['mention'] = 0
                            with open('config.yaml', 'w') as file:
                                documents = yaml.dump(cfg, file)
                            ###
                    if event.object.message['text'].lower() == 'включить упоминания' or event.object.message['text'].lower() == 'mention on':
                        if event.object.message['from_id'] == 597776932:
                            #изменение конфига
                            with open("config.yaml") as file:
                                 cfg = yaml.load(file, Loader=yaml.FullLoader)
                            cfg['mention'] = 1
                            with open('config.yaml', 'w') as file:
                                documents = yaml.dump(cfg, file)
                            ###
                    if event.object.message['text'].lower() == 'help' or event.object.message['text'].lower() == 'помощь':
                        today = datetime.datetime.today()
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + """
                            __ 0-day beta 1.0 __ 
                            
                            Команды:
                            
                            пары/пары сегодня - расписание пар сегодня
                            пары завтра - расписание пар завтра
                            пары вчера - расписание пар вчера
                            неделя - какая неделя
                            """,
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() == 'пары' or event.object.message['text'].lower() == 'пары сегодня':
                        today = datetime.datetime.today()
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[today.isocalendar()[1] % 2][today.weekday()],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() == 'пары завтра':
                        today = datetime.datetime.today()
                        tomorrow = today + datetime.timedelta(days = 1)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[tomorrow.isocalendar()[1] % 2][tomorrow.weekday()],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() == 'пары вчера':
                        today = datetime.datetime.today()
                        yesterday = today - datetime.timedelta(days = 1)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[yesterday.isocalendar()[1] % 2][yesterday.weekday()],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() == 'неделя':
                        today = datetime.datetime.today()
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + week[today.isocalendar()[1] % 2],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() == 'неделя завтра':
                        today = datetime.datetime.today()
                        tomorrow = today + datetime.timedelta(days = 1)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + week[tomorrow.isocalendar()[1] % 2],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() == 'котик':
                        try:
                            urllib.request.urlretrieve("https://thiscatdoesnotexist.com/", "img.jpg")
                            photo = vk_upl.photo_messages('img.jpg')
                            owner_id = photo[0]['owner_id']
                            photo_id = photo[0]['id']
                            access_key = photo[0]['access_key']
                            attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                        except:
                            print("Error")
                        else:
                            if event.from_chat:
                                vk.messages.send(
                                key = (''),
                                server = (''),
                                ts=(''),
                                random_id = get_random_id(),
                                message = appeal,
                                chat_id = event.chat_id,
                                attachment=attachment
                                )
                    if event.object.message['text'].lower() == 'космос':
                        try:
                            urllib.request.urlretrieve('https://firebasestorage.googleapis.com/v0/b/thisnightskydoesnotexist.appspot.com/o/images%2Fseed' + str(random.randint(1, 5001)).zfill(4) + '.jpg?alt=media', 'img.jpg')
                            photo = vk_upl.photo_messages('img.jpg')
                            owner_id = photo[0]['owner_id']
                            photo_id = photo[0]['id']
                            access_key = photo[0]['access_key']
                            attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                        except:
                            print("Error")
                        else:
                            if event.from_chat:
                                vk.messages.send(
                                key = (''),
                                server = (''),
                                ts=(''),
                                random_id = get_random_id(),
                                message = appeal,
                                chat_id = event.chat_id,
                                attachment=attachment
                                )
        except Exception as e:
            print(e)
            pass
if __name__ == '__main__':
    main()