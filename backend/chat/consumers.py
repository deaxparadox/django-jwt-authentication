import json

from channels.generic.websocket import (
    WebsocketConsumer, 
    AsyncConsumer,
    AsyncWebsocketConsumer
)


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))

class AsynChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.scope)
        print(self.scope['user'])
        await self.accept()

    async def disconnect(self, code):
        return await super().disconnect(code)

    async def receive(self, text_data):
        print(self.scope['user'])
        text_data_json = json.loads(text_data)
        # message = text_data_json["message"]
        message = "Received: " + text_data_json["message"]

        await self.send(text_data=json.dumps({"message": message}))


class AsyncEchoConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event["text"],
        })

    