import requests
import vk
import vk_api
import time
import json
import random
from bs4 import BeautifulSoup as BS
import re
import os
token = os.environ.get('vktoken')
obamavideo = 'video615903213_456239017', 'video615903213_456239018','video615903213_456239025', 'video615903213_456239024','video615903213_456239023'
meizu = 'photo615903213_457239156', 'photo615903213_457239157', 'photo615903213_457239158', 'photo615903213_457239159', 'photo615903213_457239160', 'photo615903213_457239161'
from vk_api.longpoll import VkLongPoll, VkEventType
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
creator = [323588703, 615903213, 619542867]
nfcusers = [323588703, 284742001] + creator
users = [445974783, 323588703, 284742001, 444609988, 548365367, 197753478] +  nfcusers
bl = []
album = 'photo615903213_457239073', 'photo615903213_457239072', 'photo615903213_457239071', 'photo615903213_457239070', 'photo615903213_457239069', 'photo615903213_457239068', 'photo615903213_457239067', 'photo615903213_457239066', 'photo615903213_457239065', 'photo615903213_457239064', 'photo615903213_457239063', 'photo615903213_457239062', 'photo615903213_457239061', 'photo615903213_457239060', 'photo615903213_457239059'
response = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                        method = 'messages.getLongPollServer',
                        params = 'need_pts=0&ip_version=3',
                        token = token)
                        ).json()
    
for event in longpoll.listen():
    try:
        if not event.__dict__['from'] in bl:
          text = event.__dict__
          checkid = text['from']
          if event.text.lower() == '.donate':
              resp = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.send',
                                          params = f'peer_id={event.peer_id}&random_id={0}&message=Доступ к основным командам ---> 100р. Доступ к основным командам + .nfc --->  250р. Донатить нужно сюда (qiwi.com/n/ZABIVNOY2012), в примечании укажи своё ФИО в вк или ID.&reply_to={event.message_id}',
                                          token = token)
                                          ).json()
          if int(checkid) in creator:
              if '+bl' in event.text.lower() or '-bl' in event.text.lower():
                f = event.attachments['reply']
                cid = json.loads(f)['conversation_message_id']
                response = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                  method = 'messages.getByConversationMessageId',
                                  params = 'peer_id={z}&conversation_message_ids={x}'.format(z = event.peer_id, x = cid),
                                  token = token),
                                  ).json()  
                m = response['response']['items'][0]['from_id']
                if event.text.lower() == '+bl':
                  bl.append(m)
                  blstatus = 'добавлен в чёрный список'
                if event.text.lower() == '-bl':
                  bl.remove(m)
                  blstatus = "удалён из чёрного списка."
                r = resp = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = f'peer_id={event.peer_id}&random_id={0}&message=[id{m}|Пользователь] {blstatus}&reply_to={event.message_id}',
                                              token = token)
                                              ).json()
              if event.text.lower() == '.setrole prince':
                  f = event.attachments['reply']
                  cid = json.loads(f)['conversation_message_id']
                  response = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                  method = 'messages.getByConversationMessageId',
                                  params = 'peer_id={z}&conversation_message_ids={x}'.format(z = event.peer_id, x = cid),
                                  token = token),
                                  ).json()  
                  m = response['response']['items'][0]['from_id']
                  users.append(m)
                  r = resp = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = f'peer_id={event.peer_id}&random_id={0}&message=[id{m}|Пользователю] были выданы права на основные команды. ({m})&reply_to={event.message_id}',
                                              token = token)
                                              ).json()
              if event.text.lower() == '.setrole king':
                  f = event.attachments['reply']
                  cid = json.loads(f)['conversation_message_id']
                  response = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                  method = 'messages.getByConversationMessageId',
                                  params = 'peer_id={z}&conversation_message_ids={x}'.format(z = event.peer_id, x = cid),
                                  token = token),
                                  ).json()  
                  m = response['response']['items'][0]['from_id']
                  nfcusers.append(m)
                  r = resp = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = f'peer_id={event.peer_id}&random_id={0}&message=[id{m}|Пользователю] были выданы права на все команды. ({m})&reply_to={event.message_id}',
                                              token = token)
                                              ).json()
              if event.text.lower() == '.setrole creator':
                  f = event.attachments['reply']
                  cid = json.loads(f)['conversation_message_id']
                  response = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                  method = 'messages.getByConversationMessageId',
                                  params = 'peer_id={z}&conversation_message_ids={x}'.format(z = event.peer_id, x = cid),
                                  token = token),
                                  ).json()  
                  m = response['response']['items'][0]['from_id']
                  creator.append(m)
                  r = resp = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = f'peer_id={event.peer_id}&random_id={0}&message=[id{m}|Пользователь] назначен создателем. ({m})&reply_to={event.message_id}',
                                              token = token)
                                              ).json()
              if event.text.lower() == '.clear king':
                  f = event.attachments['reply']
                  cid = json.loads(f)['conversation_message_id']
                  response = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                  method = 'messages.getByConversationMessageId',
                                  params = 'peer_id={z}&conversation_message_ids={x}'.format(z = event.peer_id, x = cid),
                                  token = token),
                                  ).json()  
                  m = response['response']['items'][0]['from_id']
                  nfcusers.remove(m)
                  r = resp = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = f'peer_id={event.peer_id}&random_id={0}&message=[id{m}|Пользователь] потерял свои права на использование команд.({m})&reply_to={event.message_id}',
                                              token = token)
                                              ).json()
              if event.text.lower() == '.clear all':
                  f = event.attachments['reply']
                  cid = json.loads(f)['conversation_message_id']
                  response = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                  method = 'messages.getByConversationMessageId',
                                  params = 'peer_id={z}&conversation_message_ids={x}'.format(z = event.peer_id, x = cid),
                                  token = token),
                                  ).json()  
                  m = response['response']['items'][0]['from_id']
                  if m in users:
                    users.remove(m)
                  if m in nfcusers:
                    nfcusers.remove(m)
                  if m in creator:
                    creator.remove(m)
                  r = resp = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = f'peer_id={event.peer_id}&random_id={0}&message=С [id{m}|пользователя] были сняты все роли.({m})&reply_to={event.message_id}',
                                              token = token)
                                              ).json()
              if event.text.lower() == '.clear prince':
                  f = event.attachments['reply']
                  cid = json.loads(f)['conversation_message_id']
                  response = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                  method = 'messages.getByConversationMessageId',
                                  params = 'peer_id={z}&conversation_message_ids={x}'.format(z = event.peer_id, x = cid),
                                  token = token),
                                  ).json()  
                  m = response['response']['items'][0]['from_id']
                  users.remove(m)
                  r = resp = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = f'peer_id={event.peer_id}&random_id={0}&message=[id{m}|Пользователь] потерял свои права на использование команд.({m})&reply_to={event.message_id}',
                                              token = token)
                                              ).json()
          if int(checkid) in users:
              if event.text.lower() == '.nfcstatus':
                      text = event.__dict__
                      checkid = text['from']
                      if int(checkid) in nfcusers:
                          print('ok')
                          resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.send',
                                          params = 'peer_id={vga}&random_id={rid}&message={oga}&reply_to={rp}'.format(vga = event.peer_id, rid = 0, rp = event.message_id, oga = 'NFCDemon v1.08 вызван!'),
                                          token = token)
                                          ).json()
                      else:
                          resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.send',
                                          params = 'peer_id={vga}&random_id={rid}&sticker_id={oga}&reply_to={rp}'.format(vga = event.peer_id, rid = 0, rp = event.message_id, oga = 99),
                                          token = token)
                                          ).json()
                          print(resp2)
              if event.text.lower() == '.nfc':
                      text = event.__dict__
                      checkid = text['from']
                      if int(checkid) in nfcusers:
                          print('ok')
                          resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.send',
                                          params = 'peer_id={vga}&random_id={rid}&message={oga}&reply_to={rp}&attachment={roja}'.format(vga = event.peer_id, rid = 0, oga = '@helio_g90t, раскрыт фрагмент твоего лица! Виновник торжества: [id'+ checkid +'|NFCMan]', rp = event.message_id, roja = random.choice(album)),
                                          token = token)
                                          ).json()
                      else:
                          resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.send',
                                          params = 'peer_id={vga}&random_id={rid}&sticker_id={oga}&reply_to={rp}'.format(vga = event.peer_id, rid = 0, rp = event.message_id, oga = 99),
                                          token = token)
                                          ).json()
                          print(resp2)
              if event.text.lower() == '.myrole':
                text = event.__dict__
                checkid = text['from']
                userid = int(checkid)
                if userid in creator:
                  role = 'создатель';
                if userid in nfcusers and userid not in creator:
                  role = 'участник NFCClub'
                if userid in users and userid not in nfcusers and userid not in creator:
                  role = 'простой мужик в трусах'
                r = resp = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = f'peer_id={event.peer_id}&random_id={0}&message=[id{m}|Ваша] роль - {role}&reply_to={event.message_id}',
                                              token = token)
                                              ).json()
              if '.honor' in event.text.lower():
                  msg = 'В Lego Village завезли партию новых дилдо. Помогите Толику потерять анальную девственность и выбросить какашку без нфс. Хонор для латексных гомосексуалистов.';
                  respik = resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                                  method = 'messages.send',
                                                  params = f'peer_id={event.peer_id}&random_id={0}&message={msg}&reply_to={event.message_id}',
                                                  token = token)
                                                  ).json() 
              if '.nw cpu' in event.text.lower():
                  if 'cpuinfo' not in event.text.lower():
                      try:
                          prc = event.text.lower()[8:].replace(' ', '-')
                          r = requests.get(f'https://nanoreview.net/ru/cpu/{prc}')
                          a = BS(r.text, 'html.parser')
                          b = a.select_one('div.exeption-container')
                          if b:
                              respik = resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                                  method = 'messages.send',
                                                  params = f'peer_id={event.peer_id}&random_id={0}&message=Произошла ошибка, проверьте, правильно ли вы ввели название, вводить его нужно полностью (Пример: Amd Ryzen 5 3600 / Intel Core i3 10100f). \n \n Ошибка: {b.text}&reply_to={event.message_id}',
                                                  token = token)
                                                  ).json() 
                          else:
                              a = a.select_one('div.two-columns')
                              a = a.text.replace('\n', '')
                              a = a.replace('\t\t\t\t', '\n')
                              respik = resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                                      method = 'messages.send',
                                                      params = f'peer_id={event.peer_id}&random_id={0}&message={a}.&reply_to={event.message_id}',
                                                      token = token)
                                                      ).json() 
                      except Exception as e:
                          print(e)
              if '.nw phone' in event.text.lower():
                  if 'phonecpu' not in event.text.lower():
                      try:
                          ph = {
                              'Geekbench 4.4 (одноядерный)': 'Неизвестно',
                              'Geekbench 4.4 (многоядерный)':'Неизвестно',
                              'Geekbench 5 (одноядерный)': 'Неизвестно',
                              'Geekbench 5 (многоядерный)': 'Неизвестно',
                              'AnTuTu Benchmark 7': ' Неизвестно',
                              'AnTuTu Benchmark 8': ' Неизвестно'
                              }
                          phone = f'{event.text.lower()[10:]}'
                          url = f'https://nanoreview.net/ru/phone/{phone.replace(" ", "-")}'
                          r = requests.get(f'https://nanoreview.net/ru/phone/{phone.replace(" ", "-")}')
                          t = BS(r.text, 'html.parser')    
                          c = t.select('span.score-bar-result-number')
                          sc = t.select('div.score-bar-name')
                          pos = 0
                          try:
                              b = t.select_one('div.exeption-container')
                              if b:
                                  c = b.select_one('h3')
                                  respik = resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = f'peer_id={event.peer_id}&random_id={0}&message=Произошла ошибка, проверьте, правильно ли вы ввели название смартфона, вводить его нужно полностью (Пример: Vivo iQOO 7 / Oppo Realme x50 5G). \n \n Ошибка: {c.text}.&reply_to={event.message_id}',
                                              token = token)
                                              ).json() 
                              else:
                                  for i in range(2,8):
                                      try:
                                          name = sc[i + 5].text
                                          result = c[i].text
                                          name = name.replace('\n', '')
                                          name = name.replace('\t', '')
                                          for f in range(len(ph.keys())):
                                              ph[name] = result
                                      except Exception:
                                          None
                                  res = list(ph.keys())[0] + ' - ' + list(ph.values())[0] + '\n' + list(ph.keys())[1] + ' —— ' + list(ph.values())[1] + '\n' + list(ph.keys())[2] + ' —— ' + list(ph.values())[2] + '\n' + list(ph.keys())[3] + ' —— ' + list(ph.values())[3] + '\n' + list(ph.keys())[4] + ' —— ' + list(ph.values())[4] + '\n' + list(ph.keys())[5] + ' —— ' + list(ph.values())[5]
                                  respik = resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                                      method = 'messages.send',
                                                      params = f'peer_id={event.peer_id}&random_id={0}&message={res}.&reply_to={event.message_id}',
                                                      token = token)
                                                      ).json()
                          except Exception as Es:
                              None
                      except Exception as Exc:
                          print(Exc)
              if '.nw cpuinfo' in event.text.lower():
                  prc = event.text.lower()[12:].replace(' ', '-')
                  r = requests.get(f'https://nanoreview.net/ru/cpu/{prc.replace(" ", "-")}')
                  bf = BS(r.text, 'html.parser')
                  b = bf.select_one('div.exeption-container')
                  if b:
                      respik = resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.send',
                                          params = f'peer_id={event.peer_id}&random_id={0}&message=Произошла ошибка, проверьте, правильно ли вы ввели название, вводить его нужно полностью (Пример: Amd Ryzen 5 3600 / Intel Core i3 10100f). \n \n Ошибка: {b.text}&reply_to={event.message_id}',
                                          token = token)
                                          ).json() 
                  else:
                      a = bf.select('table.specs-table')[1].text + bf.select('table.specs-table')[2].text + bf.select('table.specs-table')[3].text
                      a = a.replace('\n\n', '\n')
                      respik = resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.send',
                                          params = f'peer_id={event.peer_id}&random_id={0}&message={a}.&reply_to={event.message_id}',
                                          token = token)
                                          ).json()                
              if '.nw phonecpu' in event.text.lower():
                  phone = f'{event.text.lower()[13:]}'
                  r = requests.get(f'https://nanoreview.net/ru/phone/{phone.replace(" ", "-")}')
                  gf = BS(r.text, 'html.parser')
                  b = gf.select_one('div.exeption-container')
                  if b:
                      c = b.select_one('h3')
                      respik = resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                  method = 'messages.send',
                                  params = f'peer_id={event.peer_id}&random_id={0}&message=Произошла ошибка, проверьте, правильно ли вы ввели название смартфона, вводить его нужно полностью (Пример: Vivo iQOO 7 / Oppo Realme x50 5G). \n \n Ошибка: {c.text}.&reply_to={event.message_id}',
                                  token = token)
                                  ).json()
                  else: 

                      inf = gf.select('table.specs-table')
                      for el in range(len(inf)):
                        if 'процессор' not in inf[el].text.lower():
                            el += 1
                        else:
                            print(el)
                            g = inf[el].text.replace('\n\n\n', '\n')
                      respik = resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = f'peer_id={event.peer_id}&random_id={0}&message={g}&reply_to={event.message_id}',
                                              token = token)
                                              ).json()
                      else:
                          respik = resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = f'peer_id={event.peer_id}&random_id={0}&message=Неизвестная ошибка.&reply_to={event.message_id}',
                                              token = token)
                                              ).json()
              if event.text.lower() == '.meizu':
                  respik = resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.send',
                                          params = 'peer_id={vga}&random_id={rid}&message={oga}&reply_to={rp}&attachment={mph}'.format(vga = event.peer_id, rid = 0, oga = 'Иногда хочется купить мозг мейзуводам, но потом понимаешь, что их организм, как флайм, стал нестабильным.' + '\n' +  '(meizu говно)', rp = event.message_id, mph = random.choice(meizu)),
                                          token = token)
                                          ).json()
                  time.sleep(0.2)
              if event.text.lower() == '.annoyeer':
                  open('annoyeer.py')

              if event.text.lower() == '.ping' or event.text.lower() == '.пинг':
                  hostname = 'google.com'
                  ping = os.system("ping -c 1 " + hostname)
                  respik = resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.send',
                                          params = 'peer_id={vga}&random_id={rid}&message={oga}&reply_to={rp}'.format(vga = event.peer_id, rid = 0, oga = '⚙ Вычисляю пинг.   ' + '/', rp = event.message_id),
                                          token = token)
                                          ).json()
                  time.sleep(0.2)
                  resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.edit',
                                          params = 'peer_id={vga}&message_id={rid}&message={oga}&reply_to={rp}'.format(vga = event.peer_id, rid = event.message_id + 1, oga = '⚙ Вычисляю пинг..   \\', rp = event.message_id),
                                          token = token)
                                          ).json()
                  time.sleep(0.2)
                  resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.edit',
                                          params = 'peer_id={vga}&message_id={rid}&message={oga}&reply_to={rp}'.format(vga = event.peer_id, rid = event.message_id + 1, oga = '⚙ Вычисляю пинг...   |', rp = event.message_id),
                                          token = token)
                                          ).json()
                  time.sleep(0.2)
                  respik = resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.delete',
                                          params = 'message_ids={rid}&delete_for_all={oga}'.format(oga = 1, rid = event.message_id + 1),
                                          token = token)
                                          ).json()
                  resp3 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.send',
                                          params = 'peer_id={pid}&random_id={rid}&message={msg}&reply_to={rp}'.format(pid = event.peer_id, rid = 0, msg = 'Понг! Задержка: ' + str(ping) + 's', rp = event.message_id),
                                          token = token)
                                          ).json()

              text = event.__dict__
              checkid = text['from']
              if int(checkid) in users:
                  try:
                      if event.text.lower() == '.cmd':
                          cmd = '.getid(ответом) - выдаёт айди пользователя,' + '\n' + '.get(ответом) - выдаёт информацию о пользователе,' + '\n' + '.meme - кидает рандомный мем из альбома,' + '\n' + '.kick(ответом или упомянанием (kick @id)) - исключает пользователя, можно указывать причину с новой строки после команды' + '\n' + '.inv(ответом) - возвращает участника в беседу,'  + '\n' +'.pin(ответом) - закрепляет сообщение в беседе.'
                          resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.send',
                                          params = 'peer_id={vga}&random_id={rid}&message={oga}&reply_to={rp}'.format(vga = event.peer_id, rid = 0, rp = event.message_id, oga = '⚙ Доступные команды:' + '\n' + cmd),
                                          token = token)
                                          ).json()
                      if '.kick' in event.text.lower():
                          x = event.text.lower()
                          ka = re.sub(r'\|.*','', event.text.lower())[9:]                
                          if '\n' in event.text.lower():
                              msgid = re.sub(r'\n.*', '', ka)

                              reason = x[x.find('\n') + 1:]
                              resp = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.removeChatUser',
                                          params = 'chat_id={vg}&member_id={og}'.format(vg = event.chat_id, og = msgid),
                                          token = token)
                                          ).json()
                              try:
                                  g = resp['error']['error_code']
                                  print(msgid, 'Причина' + reason)
                                  print(g)
                                  print(resp)
                                  if g == 15:
                                      resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = 'peer_id={vga}&random_id={rid}&message={oga}&reply_to={rp}'.format(vga = event.peer_id, rid = 0, oga = ' ⚠ Не удалось исключить пользователя, скорее всего, у меня нет доступа, либо пользователь является администратором или создателем беседы.', rp = event.message_id),
                                              token = token)
                                              ).json()

                              except KeyError:
                                  resp3 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.send',
                                          params = 'peer_id={pid}&random_id={rr}&message={msg}'.format(pid = event.peer_id, rr = 0, msg = '[' + 'id' + str(msgid) + '|Пользователь] был исключён.' + '\n' + "Причина: " + reason),
                                          token = token)
                                          ).json()
                          if '\n' not in event.text.lower():
                              try:

                                  msgid = re.sub(r'\n.*', '', ka)
                                  reason = x[x.find('\n') + 1:]
                                  resp = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.removeChatUser',
                                          params = 'chat_id={vg}&member_id={og}'.format(vg = event.chat_id, og = msgid),
                                          token = token)
                                          ).json()
                                  g = resp['error']['error_code']
                                  print(resp)
                                  print(g)
                                  if g == 15:
                                      resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = 'peer_id={vga}&random_id={rid}&message={oga}&reply_to={rp}'.format(vga = event.peer_id, rid = 0, oga = ' ⚠ Не удалось исключить пользователя, скорее всего, у меня нет доступа, либо пользователь является администратором или создателем беседы.', rp = event.message_id),
                                              token = token)
                                              ).json()

                              except KeyError:
                                  resp3 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                          method = 'messages.send',
                                          params = 'peer_id={pid}&random_id={rr}&message={msg}'.format(pid = event.peer_id, rr = 0, msg = '[' + 'id' + str(msgid) + '|Пользователь] был исключён.' + '\n' + 'Причина: не указана.'),
                                          token = token)
                                          ).json()
                      if event.text.lower() == '.kick':
                          try:
                              f = event.attachments['reply']
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
                      if event.text.lower() == '.meme':
                          resp2 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.send',
                                              params = 'peer_id={vga}&random_id={rid}&message={oga}&reply_to={rp}&attachment={atch}'.format(vga = event.peer_id, rid = 0, oga = 'Ну ладно, вот тебе прикол бесплатно без смс и регистраций.', rp = event.message_id, atch = random.choice(obamavideo)),
                                              token = token)
                                              ).json()

                      if event.text.lower() == '.get':
                          f = event.attachments['reply']
                          print(f)
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
                          print(event.__dict__)
                          print(f)
                          cid = json.loads(f)['conversation_message_id']
                          response = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                      method = 'messages.getByConversationMessageId',
                                      params = 'peer_id={z}&conversation_message_ids={x}'.format(z = event.peer_id, x = cid),
                                      token = token),
                                      ).json()

                          m = response['response']['items'][0]['from_id']

                          resk = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                      method = 'messages.send',
                                      params = 'peer_id={v}&random_id={p}&message={o}'.format(v = event.peer_id, p = 0, o = '⚙ Достаю ID... '),
                                      token = token),
                                      ).json()
                          time.sleep(1)
                          res = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                      method = 'messages.edit',
                                      params = 'peer_id={v}&message_id={p}&message={o}'.format(v = event.peer_id, p = event.message_id + 1, o = 'ID [' + 'id' + str(m) + '|пользователя] - ' + str(m)),
                                      token = token),
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
                      if event.text.lower() == '.pin':
                          f = event.attachments['reply']
                          cid = json.loads(f)['conversation_message_id']
                          resp3 = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                              method = 'messages.pin',
                                              params = 'peer_id={vga}&conversation_message_id={cd}'.format(vga = event.peer_id, cd = cid),
                                              token = token)
                                              ).json()

                  except Exception as be:
                      None
    except Exception as es:
        None
