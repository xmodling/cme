import requests
import os
import vk
import vk_api
import time
import json
import random
token = os.environ.get('vktoken')
from vk_api.longpoll import VkLongPoll, VkEventType
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
response = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                        method = 'messages.getLongPollServer',
                        params = 'need_pts=0&ip_version=3',
                        token = token)
                        ).json()
for event in longpoll.listen():
    if event.from_me:
        try:
            if event.text.lower() == '.get':
                f = event.attachments['reply']
                cid = json.loads(f)['conversation_message_id']
                response1 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                    method = 'messages.getByConversationMessageId',
                                    params = 'peer_id={z}&conversation_message_ids={x}'.format(z = event.peer_id, x = cid),
                                    token = token),
                                    ).json()
                m = response1['response']['items'][0]['from_id']
                uget = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                    method = 'users.get',
                                    params = 'user_ids={vga}&fields={fi}&reply_to={rp}'.format(vga = m, fi = 'sex,verified,online', rp = event.message_id),
                                    token = token)
                                    ).json()
                first_name = uget['response'][0]['first_name']
                last_name = uget['response'][0]['last_name']
                name = first_name + ' ' + last_name
                online = uget['response'][0]['online']
                checkg = uget['response'][0]['verified']
                sex = uget['response'][0]['sex']
                
                if online == 1:
                    yes = 'онлайн 🎾'
                if online == 0:
                    yes = 'оффлайн 🛑'
                if checkg == 1:
                    galka = 'имеется ✅'
                if checkg == 0:
                    galka = 'не имеется 🚫'
                if sex == 1:
                    pol = 'женский 👩‍🦰'
                if sex == 2:
                    pol = 'мужской 🧔'
                if sex == 0:
                    pol = '🛌 не указан'
                ff = '🔔 Информация о [' + 'id' + str(m) + '|пользователе]:' + '\n' + '‍👮‍ ФИО: ' + name + '\n' + '🌏 Состояние: ' + yes + '\n' + '🛀 Пол: ' + pol + '\n' + '⚙ Верификация: ' + galka
                reskf = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                method = 'messages.send',
                                params = 'peer_id={v}&random_id={p}&message={o}'.format(v = event.peer_id, p = 0, o = '⚙ Запрашиваю информацию...'),
                                token = token),
                                ).json()
                time.sleep(3)
                resp3 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                            method = 'messages.edit',
                            params = 'peer_id={pid}&message_id={rr}&message={msg}'.format(pid = event.peer_id, rr = event.message_id + 1, msg = ff),
                            token = token)
                            ).json()
            if 'волкобот кто' in event.text.lower():
        
                if event.from_chat:
                    response = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                method = 'messages.getChat',
                                params = 'chat_id={z}'.format(z = event.chat_id),
                                token = token),
                                ).json()

                    uid = response['response']['users']
                    ruid = random.choice(uid)
                    print(ruid)
                    us = event.text.lower()[12:]
                    resk = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                method = 'messages.send',
                                params = 'peer_id={v}&random_id={p}&message={o}'.format(v = event.peer_id, p = 0, o = '⚙ Получаю ответ от мудрого волка... '),
                                token = token),
                                ).json()
                    time.sleep(2)
                    response = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                method = 'messages.edit',
                                params = 'peer_id={z}&message_id={mid}&message={msg}'.format(z = event.peer_id, mid = event.message_id + 1, msg = 'Волкобот сказал, что ' + '[id' + str(ruid) + '|он(а)] ' + us + '.'),
                                token = token),
                                ).json()
                else: 
                         reskf = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                method = 'messages.send',
                                params = 'peer_id={v}&random_id={p}&message={o}'.format(v = event.peer_id, p = 0, o = '⚠ В чате всего два человека, лучше решите этот вопрос сами, чем беспокоить мудрого волка.'),
                                token = token),
                                ).json()
                        
                print(response.keys())
                print("Получено сообщение")
            rep = event.attachments['reply']
            f = event.attachments['reply']

            if event.text.lower() == '.getid':
                print(event.peer_id)
                cid = json.loads(f)['conversation_message_id']
                response = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                            method = 'messages.getByConversationMessageId',
                            params = 'peer_id={z}&conversation_message_ids={x}'.format(z = event.peer_id, x = cid),
                            token = token),
                            ).json()
                
                m = response['response']['items'][0]['from_id']
                
                resk = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                            method = 'messages.edit',
                            params = 'peer_id={v}&message_id={p}&message={o}'.format(v = event.peer_id, p = event.message_id, o = '⚙ Достаю ID... '),
                            token = token),
                            ).json()
                time.sleep(1)
                res = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                            method = 'messages.edit',
                            params = 'peer_id={v}&message_id={p}&message={o}'.format(v = event.peer_id, p = event.message_id, o = 'ID [' + 'id' + str(m) + '|пользователя] - ' + str(m)),
                            token = token),
                            ).json()
            if event.text.lower() == '.kick':
                try:
                    cid = json.loads(f)['conversation_message_id']
                
                    response1 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                method = 'messages.getByConversationMessageId',
                                params = 'peer_id={z}&conversation_message_ids={x}'.format(z = event.peer_id, x = cid),
                                token = token),
                                ).json()
                
                    m = response1['response']['items'][0]['from_id']

                    resp = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                method = 'messages.removeChatUser',
                                params = 'chat_id={vg}&member_id={og}'.format(vg = event.chat_id, og = m),
                                token = token)
                                ).json()

                    g = resp['error']['error_code']

                    if g == 15:
                        resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                method = 'messages.send',
                                params = 'peer_id={vga}&random_id={rid}&message={oga}&reply_to={rp}'.format(vga = event.peer_id, rid = 0, oga = ' ⚠ Не удалось исключить пользователя, скорее всего, у меня нет доступа, либо пользователь является администратором или создателем беседы.', rp = event.message_id),
                                token = token)
                                ).json()

                except KeyError:
                    resp3 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                            method = 'messages.send',
                            params = 'peer_id={pid}&random_id={rr}&message={msg}'.format(pid = event.peer_id, rr = 0, msg = '[' + 'id' + str(m) + '|Пользователь] был исключён.'),
                            token = token)
                            ).json()
            if event.text.lower() == '.inv':
                try:
                    cid = json.loads(f)['conversation_message_id']
                    response1 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                    method = 'messages.getByConversationMessageId',
                                    params = 'peer_id={z}&conversation_message_ids={x}'.format(z = event.peer_id, x = cid),
                                    token = token),
                                    ).json()
                
                    m = response1['response']['items'][0]['from_id']
                    resp = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                    method = 'messages.addChatUser',
                                    params = 'chat_id={vg}&user_id={og}'.format(vg = event.chat_id, og = m),
                                    token = token)
                                    ).json()
                    invno = resp['error']['error_text']
                    if 'уже в ней' in invno:
                        resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                method = 'messages.send',
                                params = 'peer_id={vga}&random_id={rid}&message={oga}&reply_to={rp}'.format(vga = event.peer_id, rid = 0, oga =  '⚠ Пользователь уже находится в беседе. (15)', rp = event.message_id),
                                token = token)
                                ).json()
                    
                        
                except KeyError as E:
                    try:
                        print(E)
                        invadm = resp['error']['error_code']
                        print(invadm)
                        if invadm == 925:

                            resp3 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                    method = 'messages.send',
                                    params = 'peer_id={vga}&random_id={rid}&message={oga}&reply_to={rp}'.format(vga = event.peer_id, rid = 0, oga =  '⚠ Невозможно пригласить пользователя, так как у меня нет доступа. (925)', rp = event.message_id),
                                    token = token)
                                    ).json()
                    except KeyError: 
                        resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                    method = 'messages.send',
                                    params = 'peer_id={vga}&random_id={rid}&message={oga}&reply_to={rp}'.format(vga = event.peer_id, rid = 0, oga = '[id' +  str(m) + '|Пользователю] успешно отправлено приглашение', rp = event.message_id),
                                    token = token)
                                    ).json()

        except Exception as er:
            print(er)
            None
