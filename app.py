from flask import Flask, request
from message import VkApi


api = VkApi('22e5ccbfe6f72548fc6579a21c57889e224582263cc9c4da2085be1281c8e00d0435912eb0b1fe021a4f2')


app = Flask(__name__)
@app.route('/vk/', methods=['POST'])
def vk():
    message = request.get_json()

    if message.get('type') == 'confirmation':
        return '9ae03106'

    if message.get('type') == 'message_new':
        api.message(
            message.get('object').get('from_id'), 
            message.get('object').get('text')
        )
        return 'Ok'