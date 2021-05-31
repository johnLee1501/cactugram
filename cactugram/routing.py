from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path


from cactus.consumers import CactusConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path(r'ws/cactus', CactusConsumer.as_asgi()),
        ])
    ),
})
