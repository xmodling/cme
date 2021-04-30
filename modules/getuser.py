from bs4 import BeautifulSoup
import requests, vk_api
token = "ccb00173d59e541c1f01b9fce4748fcd95425c1b15a3a2d425fb4196ca6d4373fb7d65bb52f87b5bf9bce"
from vk_api.longpoll import VkLongPoll, VkEventType
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
class UserInfo:
    def getUser(event, token):
        soup = BeautifulSoup(requests.get(f'https://vk.com/foaf.php?id={event.__dict__["info"]["user_id"]}').text, 
        'lxml').find('ya:created').get('dc:date')
        user = requests.get(
            'https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(method = 'users.get',params = f'user_id={event.__dict__["info"]["user_id"]}&fields=counters',token = token)
            ).json()['response'][0]['counters']
            
        user = f'''
🔎 Информация об [id{event.__dict__["info"]["user_id"]}|участнике]:
📅 Дата регистрации: {soup[:soup.find("T")]}, {soup[soup.find("T")+1:soup.find("+")]}

🧭 Активность:
Количество друзей: {user["friends"]} ({user["online_friends"]} - онлайн)
Количество аудиозаписей: {user["audios"]}
🔮 На странице {user["videos"]} видеозаписей и {user["photos"]} фотографий.
'''
        requests.get('https://api.vk.com/method/messages.send?{params}&access_token={token}&v=5.95'.format(params = f'random_id=0&peer_id={event.peer_id}&message={user}',token = token))
