from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from map_app import consumer

websocket_urlPattern = [
    path('ws/polData/', consumer.CustomerDashboardConsumer.as_asgi()),
]
application = ProtocolTypeRouter ({
   'websocket': AuthMiddlewareStack(URLRouter(
       websocket_urlPattern
   ))
})