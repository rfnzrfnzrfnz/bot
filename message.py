from requests import post


class VkApi:
    token = ''
    url ='https://api.vk.com/method/{}'

    def __init__(self, token):
        self.token = token
    def message(self, user_id, message):
        result = post(a.url.format('messages.send'), {
            'access_token':'22e5ccbfe6f72548fc6579a21c57889e224582263cc9c4da2085be1281c8e00d0435912eb0b1fe021a4f2',
            'v':'5.82',
            'user_id': user_id,
            'message': message
        })
        return result.json()




a = VkApi("tokenrhjymyugyt")
b = a.message(298224977,"сегодня будут эти мероприятия")
print(repr(b))