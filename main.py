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
import config
import re
import traceback
import sys
#from autocorrect import Speller

def isBanned(id):
    with open("config.yaml", 'r') as stream:
        cfg = yaml.load(stream, Loader=yaml.FullLoader)
    banned = cfg['banned']
    if id in banned:
        return 1
    else:
        return 0
tz = pytz.timezone('Europe/Moscow')
#spell = Speller('ru')
#vk.messages.send(peer_id=event.object.peer_id, random_id=0, attachment=attachment)

table = config.table

week = {0 : 'Знаменатель (четная неделя)', 1 : 'Числитель (нечетная неделя)'}
#message = table[datetime.datetime.today().isocalendar()[1] % 2][datetime.datetime.today().weekday()]
with open("config.yaml", 'r') as stream:
    cfg = yaml.load(stream, Loader=yaml.FullLoader)
token = cfg['token']

def main():
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    vk_upl = vk_api.VkUpload(vk)
    while True:
        try:
            longpoll = VkBotLongPoll(vk_session, '202763223')
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    user_id = event.object.message['from_id']
                    #print(event.object.message)
                    with open("config.yaml") as file:
                         cfg = yaml.load(file, Loader=yaml.FullLoader)
                    if cfg['mention'] == 0:
                        appeal = ''
                    else:
                        first_name = vk.users.get(user_ids = (user_id))[0]['first_name']
                        appeal = '[id%i|%s]' % (user_id, first_name)
                    with open("config.yaml", 'r') as stream:
                        cfg = yaml.load(stream, Loader=yaml.FullLoader)
                    banned = cfg['banned']
                    #current_message = spell(event.object.message['text']).lower()
                    current_message = event.object.message['text'].lower()
                    if current_message == 'включить упоминания' or current_message == 'mention on':
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
                    if current_message == 'отключить упоминания' or current_message == 'mention off':
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
                    if current_message == 'включить котик' or current_message == 'cat on':
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
                    if current_message == 'отключить котик' or current_message == 'cat off':
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
                    if current_message == 'включить космос' or current_message == 'space on':
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
                    if current_message == 'отключить космос' or current_message == 'space off':
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
                    if current_message == 'включить картина' or current_message == 'art on':
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
                    if current_message == 'отключить картина' or current_message == 'art off':
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
                    if current_message == 'help' or current_message == 'помощь':
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
                        today = datetime.datetime.today()
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = appeal + config.rules,
                            chat_id = event.chat_id
                            )
                    if current_message in ['пары сегодня', 'пары', 'расписание', 'расписание сегодня']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары завтра', 'расписание завтра']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары послезавтра', 'расписание послезавтра']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары послепослезавтра', 'расписание послепослезавтра']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары вчера', 'расписание вчера']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары позавчера', 'расписание позавчера']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары позапозавчера', 'расписание позапозавчера']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары в понедельник', 'расписание в понедельник', 'пары в пн', 'расписание в пн', 'пары понедельник', 'расписание понедельник', 'пары пн', 'расписание пн']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары во вторник', 'расписание во вторник', 'пары во вт', 'расписание во вт', 'пары в вторник', 'расписание в вторник', 'пары в вт', 'расписание в вт', 'пары ввторник', 'расписание вторник', 'пары вт', 'расписание вт']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары в среду', 'расписание в среду', 'пары во ср', 'расписание ср', 'пары среда', 'расписание среда', 'пары ср', 'расписание ср']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары в четверг', 'расписание в четверг', 'пары в чт', 'расписание в чт', 'пары четверг', 'расписание четверг', 'пары чт', 'расписание чт']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары в пятницу', 'расписание в пятницу', 'пары в пт', 'расписание в пт', 'пары пятница', 'расписание пятница', 'пары пт', 'расписание пт']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары в субботу', 'расписание в субботу', 'пары в сб', 'расписание в сб', 'пары суббота', 'расписание суббота', 'пары сб', 'расписание сб']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары в воскресенье', 'расписание в воскресенье', 'пары в вс', 'расписание вс', 'пары воскресенье', 'расписание воскресенье', 'пары вс', 'расписание вс']:
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message == 'неделя':
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message == 'неделя завтра':
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message in ['пары отменить', 'отменить пары']:
                        if event.from_chat:
                            vk.messages.send(
                            key = (''),
                            server = (''),
                            ts=(''),
                            random_id = get_random_id(),
                            message = "Отказано в доступе.",
                            chat_id = event.chat_id
                            )
                    if current_message == 'котик' or current_message == 'cat':
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message == 'космос' or current_message == 'space':
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if current_message == 'картина' or current_message == 'art':
                        if isBanned(user_id):
                            if event.from_chat:
                                vk.messages.send(
                                    key=(''),
                                    server=(''),
                                    ts=(''),
                                    random_id=get_random_id(),
                                    message='sorry, you\'re banned',
                                    chat_id=event.chat_id
                                )
                            continue
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
                    if 'unban' in current_message or 'разбан' in current_message:
                        if event.object.message['from_id'] == 597776932:
                            msg = current_message
                            idflag = 0
                            if 'reply_message' in event.object.message:
                                id = event.object.message['reply_message']['from_id']
                                idflag = 1
                            else:
                                try:
                                    id = int((re.search(r'\[(.*?)\|', msg).group(1))[2:])
                                    idflag = 1
                                except:
                                    pass
                            if idflag:
                                #print(id)
                                # изменение конфига
                                with open("config.yaml") as file:
                                    cfg = yaml.load(file, Loader=yaml.FullLoader)
                                if id in cfg['banned']:
                                    cfg['banned'].remove(id)
                                    with open('config.yaml', 'w') as file:
                                        documents = yaml.dump(cfg, file)
                                    if event.from_chat:
                                        vk.messages.send(
                                            key=(''),
                                            server=(''),
                                            ts=(''),
                                            random_id=get_random_id(),
                                            message='a user with an id%i was unbanned' % id,
                                            chat_id=event.chat_id
                                        )
                                else:
                                    if event.from_chat:
                                        vk.messages.send(
                                            key=(''),
                                            server=(''),
                                            ts=(''),
                                            random_id=get_random_id(),
                                            message='a user with an id%i is already unbanned' % id,
                                            chat_id=event.chat_id
                                        )
                    if ('ban' in current_message or 'бан' in current_message) and ('unban' not in current_message and 'разбан' not in current_message):
                        if event.object.message['from_id'] == 597776932:
                            msg = current_message
                            idflag = 0
                            if 'reply_message' in event.object.message:
                                id = event.object.message['reply_message']['from_id']
                                idflag = 1
                            else:
                                try:
                                    id = int((re.search(r'\[(.*?)\|', msg).group(1))[2:])
                                    idflag = 1
                                except:
                                    pass
                            if idflag:
                                #print(id)
                                # изменение конфига
                                with open("config.yaml") as file:
                                    cfg = yaml.load(file, Loader=yaml.FullLoader)
                                if id not in cfg['banned']:
                                    cfg['banned'].append(id)
                                    with open('config.yaml', 'w') as file:
                                        documents = yaml.dump(cfg, file)
                                    if event.from_chat:
                                        vk.messages.send(
                                            key=(''),
                                            server=(''),
                                            ts=(''),
                                            random_id=get_random_id(),
                                            message='a user with an id%i was banned' % id,
                                            chat_id=event.chat_id
                                        )
                                else:
                                    if event.from_chat:
                                        vk.messages.send(
                                            key=(''),
                                            server=(''),
                                            ts=(''),
                                            random_id=get_random_id(),
                                            message='a user with an id%i is already banned' % id,
                                            chat_id=event.chat_id
                                        )
        except Exception as e:
            print(traceback.format_exc())
            print(sys.exc_info()[2])
if __name__ == '__main__':
    main()
