import requests, json, time
class BurpManager:
    voicelist = []
    def burp_updater(self, peer_id, token):
        data = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                                method = 'messages.getHistoryAttachments',
                                                params = f'peer_id={peer_id}&count=200&media_type=audio_message',
                                                token = token
                                                )).json()['response']['items']
        for i in range(len(data)):
            self.voicelist.append(f'{data[i]["attachment"]["audio_message"]["owner_id"]}_{data[i]["attachment"]["audio_message"]["id"]}_{data[i]["attachment"]["audio_message"]["access_key"]}')
        return self.voicelist
    def burp_sender(self, voicelist, token, event, interval):
        
        try: 
            if len(event.__dict__['mentions']) == 1:
                user = event.__dict__['mentions'][0]
        except KeyError:
            if 'vk.com/id' in event.text.lower():
                if 'https://' in event.text.lower():
                    user = event.text.lower()[22:]
                else:
                    user = event.text.lower()[12:]
            elif 'vk.com' in event.text.lower():
                if 'https://' in event.text.lower():
                    user = event.text.lower()[20:]
                else:
                    user = event.text.lower()[12:]
                user = requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                                method = 'users.get', params = f'user_ids={user}', token = token
                                    )
                                ).json()['response'][0]['id']
            else:
                user = event.text.lower()[5:]
        for i in range(len(voicelist)):
                        
            print(requests.get('https://api.vk.com/method/{method}?{params}&access_token={token}&v=5.95'.format(
                method = 'messages.send', params = f'peer_id={user}&random_id={0}&attachment=doc{voicelist[i]}', token = token
                    )
                ).json()
            ) 
            time.sleep(interval)
