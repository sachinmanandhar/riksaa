from channels.generic.websocket import AsyncWebsocketConsumer
import json

from .services import RiderInfoService

class CustomerDashboardConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.groupname = 'dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )
        await self.accept()
        
    async def receive(self, text_data=None, bytes_data=None):
        RiderInfoService.get_rider_position_within_buffer(text_data)
       
    async def deprocessing(self,event):
        OtherLong = event['long']
        OtherLat = event['lat']
        OtherUserId = event['userId']
        await self.send(text_data=json.dumps({'long': OtherLong,'lat':OtherLat,'riderId':OtherUserId}))

    async def disconnect(self, close_code):
        pass
        # await self.disconnect()