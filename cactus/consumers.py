from django.contrib.auth.models import User
from djangochannelsrestframework.consumers import AsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer

from cactus.models import CactusModel
from cactus.serializers import CactusSerializer


class CactusConsumer(AsyncAPIConsumer):

    async def connect(self):
        await self.model_change.subscribe()
        return await super().connect()

    @model_observer(CactusModel)
    async def model_change(self, message, action=None, **kwargs):
        await self.send_json(message)

    @model_change.serializer
    def model_serialize(self, instance, action, **kwargs):
        cactus_serializer = CactusSerializer(instance)
        return cactus_serializer.data
