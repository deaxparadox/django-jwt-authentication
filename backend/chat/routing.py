from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    # re_path(r"chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    path("chat/", consumers.AsynChatConsumer.as_asgi(), name="chat")
]