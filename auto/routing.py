from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from map_app import consumer

websocket_urlPattern = [
    path('ws/rider_on/', consumer.CustomerDashboardConsumer.as_asgi()),
    path('ws/booking_request/', consumer.BookingRequestConsumer.as_asgi())  
]
application = ProtocolTypeRouter ({
   'websocket': AuthMiddlewareStack(URLRouter(
       websocket_urlPattern
   ))
})