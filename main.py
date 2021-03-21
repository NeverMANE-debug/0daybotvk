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
import pytz

tz = pytz.timezone('Europe/Moscow')

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
Физика (522)
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
1 - Яз. програм. (383)
2 - Экология (501)
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
                    if event.object.message['text'].lower() == 'включить упоминания' or event.object.message['text'].lower() == 'mention on':
                        if event.object.message['from_id'] == 597776932:
                            #изменение конфига
                            with open("config.yaml") as file:
                                 cfg = yaml.load(file, Loader=yaml.FullLoader)
                            cfg['mention'] = 1
                            with open('config.yaml', 'w') as file:
                                documents = yaml.dump(cfg, file)
                            ###
                            if event.from_chat:
                                vk.messages.send(
                                key = (''),
                                server = (''),
                                ts=(''),
                                random_id = get_random_id(),
                                message = 'tweak mention turned on',
                                chat_id = event.chat_id
                                )
                    if event.object.message['text'].lower() == 'отключить упоминания' or event.object.message['text'].lower() == 'mention off':
                        if event.object.message['from_id'] == 597776932:
                            #изменение конфига
                            with open("config.yaml") as file:
                                 cfg = yaml.load(file, Loader=yaml.FullLoader)
                            cfg['mention'] = 0
                            with open('config.yaml', 'w') as file:
                                documents = yaml.dump(cfg, file)
                            ###
                            if event.from_chat:
                                vk.messages.send(
                                key = (''),
                                server = (''),
                                ts=(''),
                                random_id = get_random_id(),
                                message = 'tweak mention turned off',
                                chat_id = event.chat_id
                                )
                    if event.object.message['text'].lower() == 'включить котик' or event.object.message['text'].lower() == 'cat on':
                        if event.object.message['from_id'] == 597776932:
                            #изменение конфига
                            with open("config.yaml") as file:
                                 cfg = yaml.load(file, Loader=yaml.FullLoader)
                            cfg['cat'] = 1
                            with open('config.yaml', 'w') as file:
                                documents = yaml.dump(cfg, file)
                            ###
                            if event.from_chat:
                                vk.messages.send(
                                key = (''),
                                server = (''),
                                ts=(''),
                                random_id = get_random_id(),
                                message = 'tweak cat turned on',
                                chat_id = event.chat_id
                                )
                    if event.object.message['text'].lower() == 'отключить котик' or event.object.message['text'].lower() == 'cat off':
                        if event.object.message['from_id'] == 597776932:
                            #изменение конфига
                            with open("config.yaml") as file:
                                 cfg = yaml.load(file, Loader=yaml.FullLoader)
                            cfg['cat'] = 0
                            with open('config.yaml', 'w') as file:
                                documents = yaml.dump(cfg, file)
                            ###
                            if event.from_chat:
                                vk.messages.send(
                                key = (''),
                                server = (''),
                                ts=(''),
                                random_id = get_random_id(),
                                message = 'tweak cat turned off',
                                chat_id = event.chat_id
                                )
                    if event.object.message['text'].lower() == 'включить космос' or event.object.message['text'].lower() == 'space on':
                        if event.object.message['from_id'] == 597776932:
                            #изменение конфига
                            with open("config.yaml") as file:
                                 cfg = yaml.load(file, Loader=yaml.FullLoader)
                            cfg['space'] = 1
                            with open('config.yaml', 'w') as file:
                                documents = yaml.dump(cfg, file)
                            ###
                            if event.from_chat:
                                vk.messages.send(
                                key = (''),
                                server = (''),
                                ts=(''),
                                random_id = get_random_id(),
                                message = 'tweak space turned on',
                                chat_id = event.chat_id
                                )
                    if event.object.message['text'].lower() == 'отключить космос' or event.object.message['text'].lower() == 'space off':
                        if event.object.message['from_id'] == 597776932:
                            #изменение конфига
                            with open("config.yaml") as file:
                                 cfg = yaml.load(file, Loader=yaml.FullLoader)
                            cfg['space'] = 0
                            with open('config.yaml', 'w') as file:
                                documents = yaml.dump(cfg, file)
                            ###
                            if event.from_chat:
                                vk.messages.send(
                                key = (''),
                                server = (''),
                                ts=(''),
                                random_id = get_random_id(),
                                message = 'tweak space turned off',
                                chat_id = event.chat_id
                                )
                    if event.object.message['text'].lower() == 'включить картина' or event.object.message['text'].lower() == 'art on':
                        if event.object.message['from_id'] == 597776932:
                            #изменение конфига
                            with open("config.yaml") as file:
                                 cfg = yaml.load(file, Loader=yaml.FullLoader)
                            cfg['art'] = 1
                            with open('config.yaml', 'w') as file:
                                documents = yaml.dump(cfg, file)
                            ###
                            if event.from_chat:
                                vk.messages.send(
                                key = (''),
                                server = (''),
                                ts=(''),
                                random_id = get_random_id(),
                                message = 'tweak art turned on',
                                chat_id = event.chat_id
                                )
                    if event.object.message['text'].lower() == 'отключить картина' or event.object.message['text'].lower() == 'art off':
                        if event.object.message['from_id'] == 597776932:
                            #изменение конфига
                            with open("config.yaml") as file:
                                 cfg = yaml.load(file, Loader=yaml.FullLoader)
                            cfg['art'] = 0
                            with open('config.yaml', 'w') as file:
                                documents = yaml.dump(cfg, file)
                            ###
                            if event.from_chat:
                                vk.messages.send(
                                key = (''),
                                server = (''),
                                ts=(''),
                                random_id = get_random_id(),
                                message = 'tweak art turned off',
                                chat_id = event.chat_id
                                )
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

[            
пары / пары сегодня
пары завтра
пары вчера
пары послезавтра
пары позавчера
пары послепослезавтра
пары позапозавчера
]

[
неделя - какая неделя (четная, нечетная)
]

[
пары в [день недели] - расписание в соответствующий день недели
]
                            """,
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() in ['пары сегодня', 'пары', 'расписание', 'расписание сегодня']:
                        today = datetime.datetime.now(tz)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[today.isocalendar()[1] % 2][today.weekday()],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() in ['пары завтра', 'расписание завтра']:
                        today = datetime.datetime.now(tz)
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
                    if event.object.message['text'].lower() in ['пары послезавтра', 'расписание послезавтра']:
                        today = datetime.datetime.now(tz)
                        tomorrow = today + datetime.timedelta(days = 2)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[tomorrow.isocalendar()[1] % 2][tomorrow.weekday()],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() in ['пары послепослезавтра', 'расписание послепослезавтра']:
                        today = datetime.datetime.now(tz)
                        tomorrow = today + datetime.timedelta(days = 3)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[tomorrow.isocalendar()[1] % 2][tomorrow.weekday()],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() in ['пары вчера', 'расписание вчера']:
                        today = datetime.datetime.now(tz)
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
                    if event.object.message['text'].lower() in ['пары позавчера', 'расписание позавчера']:
                        today = datetime.datetime.now(tz)
                        yesterday = today - datetime.timedelta(days = 2)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[yesterday.isocalendar()[1] % 2][yesterday.weekday()],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() in ['пары позапозавчера', 'расписание позапозавчера']:
                        today = datetime.datetime.now(tz)
                        yesterday = today - datetime.timedelta(days = 3)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[yesterday.isocalendar()[1] % 2][yesterday.weekday()],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() in ['пары в понедельник', 'расписание в понедельник', 'пары в пн', 'расписание в пн']:
                        today = datetime.datetime.now(tz)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[today.isocalendar()[1] % 2][0],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() in ['пары во вторник', 'расписание во вторник', 'пары во вт', 'расписание во вт', 'пары в вторник', 'расписание в вторник', 'пары в вт', 'расписание в вт']:
                        today = datetime.datetime.now(tz)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[today.isocalendar()[1] % 2][1],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() in ['пары в среду', 'расписание в среду', 'пары во ср', 'расписание в ср']:
                        today = datetime.datetime.now(tz)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[today.isocalendar()[1] % 2][2],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() in ['пары в четверг', 'расписание в четверг', 'пары в чт', 'расписание в чт']:
                        today = datetime.datetime.now(tz)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[today.isocalendar()[1] % 2][3],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() in ['пары в пятницу', 'расписание в пятницу', 'пары в пт', 'расписание в пт']:
                        today = datetime.datetime.now(tz)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[today.isocalendar()[1] % 2][4],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() in ['пары в субботу', 'расписание в субботу', 'пары в сб', 'расписание в сб']:
                        today = datetime.datetime.now(tz)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[today.isocalendar()[1] % 2][5],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() in ['пары в воскресенье', 'расписание в воскресенье', 'пары в вс', 'расписание в вс']:
                        today = datetime.datetime.now(tz)
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + table[today.isocalendar()[1] % 2][6],
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() == 'неделя':
                        today = datetime.datetime.now(tz)
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
                        today = datetime.datetime.now(tz)
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
                    if event.object.message['text'].lower() in ['пары отменить', 'отменить пары']:
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = "Отказано в доступе.",
                            chat_id = event.chat_id
                            )
                    if event.object.message['text'].lower() == 'котик' or event.object.message['text'].lower() == 'cat':
                        with open("config.yaml") as file:
                             cfg = yaml.load(file, Loader=yaml.FullLoader)
                        if cfg['cat'] == 1:
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
                    if event.object.message['text'].lower() == 'космос' or event.object.message['text'].lower() == 'space':
                        with open("config.yaml") as file:
                             cfg = yaml.load(file, Loader=yaml.FullLoader)
                        if cfg['space'] == 1:
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
                    if event.object.message['text'].lower() == 'картина' or event.object.message['text'].lower() == 'art':
                        with open("config.yaml") as file:
                             cfg = yaml.load(file, Loader=yaml.FullLoader)
                        if cfg['art'] == 1:
                            try:
                                urllib.request.urlretrieve('https://thisartworkdoesnotexist.com/', 'img.jpg')
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
