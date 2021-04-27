import requests, json, time
class BurpManager:
    def main(self):
        return self
    def burp_sender(token, event, interval):
        voicelist = [
        "575410091_595602721_aa1bb6f0cf8df80b21",
        "575410091_595328931_4f7547ac8f6bffa308",
        "575410091_595602874_93e452f4cb0ef492ee",
        "575410091_595328951_382bd57aac13d443bb",
        "575410091_595602888_a95967605fe8cf5f73",
        "575410091_595602908_15fd5aaf2c79368eb9",
        "575410091_595602908_15fd5aaf2c79368eb9",
        ]
        try: 
            if len(event.__dict__['mentions']) == 1:
                user = event.__dict__['mentions'][0]
        except KeyError:
            if 'vk.com/id' in event.text.lower():
                if 'https://' in event.text.lower():
                    user = event.text.lower()[23:]
                else:
                    user = event.text.lower()[13:]
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
