from bs4 import BeautifulSoup
import requests
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
        print(requests.get('https://api.vk.com/method/messages.send?{params}&access_token={token}&v=5.95'.format(params = f'random_id=0&peer_id={event.peer_id}&message={user}',token = token)).json())
