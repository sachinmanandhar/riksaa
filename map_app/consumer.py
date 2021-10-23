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
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'long':long,
                'lat':lat
            }
        )
        print('TextData=>',text_data)
        # pass
        # await super().receive(text_data=text_data, bytes_data=bytes_data)
<<<<<<< HEAD
=======
        
>>>>>>> 628e853ac584df5a4264359e160e0a0610ef8ee4
    async def deprocessing(self,event):
        OtherLong = event['long']
        OtherLat = event['lat']
        await self.send(text_data=json.dumps({'long': OtherLong,'lat':OtherLat}))
    async def disconnect(self, close_code):
        pass
        # await self.disconnect()