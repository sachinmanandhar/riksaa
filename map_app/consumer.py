from channels.generic.websocket import AsyncWebsocketConsumer
import json


class DashConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.groupname = 'dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )
        await self.accept()
        
    async def receive(self, text_data=None, bytes_data=None):
        datapoint = json.loads(text_data)
        long = datapoint['long']
        lat = datapoint['lat']
        userId = datapoint['user']
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':"rider_position_buffer",
                'long':long,
                'lat':lat,
                'userId':userId
            }
        )
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'long':long,
                'lat':lat,
                'userId':userId
            }
        )
        print('TextData=>',text_data)
        # pass
        # await super().receive(text_data=text_data, bytes_data=bytes_data)
    async def rider_position_buffer(self,event):
        print(event)
    async def deprocessing(self,event):
        OtherLong = event['long']
        OtherLat = event['lat']
        OtherUserId = event['userId']
        await self.send(text_data=json.dumps({'long': OtherLong,'lat':OtherLat,'riderId':OtherUserId}))
    async def disconnect(self, close_code):
        pass
        # await self.disconnect()