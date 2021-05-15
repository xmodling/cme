import json, requests
class AntiFake:
    def fake_filter(event, token):
        if requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(method = 'users.get',params = f'user_id={event.__dict__["info"]["user_id"]}&fields=counters',token = token)).json()['response'][0]['counters']['friends'] < 10:
            requests.get('https://api.vk.com/method/messages.send?{params}&access_token={token}&v=5.95'.format(params = f'random_id=0&peer_id={event.peer_id}&message=!permban @id{event.__dict__["info"]["user_id"]} \nФейк',token = token))
