from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.contrib.gis.geos import Point
from auth_app.models import Rider
from asgiref.sync import async_to_sync,sync_to_async

class CustomerDashboardConsumer(AsyncWebsocketConsumer):
    
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

        
        # rider.save()

        # if rider:
        #     rider.long = long
        #     rider.lat = lat
        #     rider.loc = Point(long,lat)
        #     rider.save()
        # else:
        #     r = await Rider(user = userId,long = long,lat=lat,loc = Point(long,lat))
        #     r.save()
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':"rider_position",
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

    # def _update_rider(self,userId,long,lat):
    #     return Rider.objects.filter(user_id =userId).update(loc = Point(long,lat))

    @sync_to_async
    def rider_position(self,event):

        # sync_to_async(self._update_rider(event["userId"],event["long"],event["lat"]))
        Rider.objects.filter(user_id =event["userId"]).update(loc = Point(event["long"],event["lat"],srid=4326))
        

    async def deprocessing(self,event):
        OtherLong = event['long']
        OtherLat = event['lat']
        OtherUserId = event['userId']
        await self.send(text_data=json.dumps({'long': OtherLong,'lat':OtherLat,'riderId':OtherUserId}))

    async def disconnect(self, close_code):

        pass
        # await self.disconnect()

class BookingRequestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.groupname = 'consumer_request'
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
        

        # print(long,lat,userId,buffer)
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':"buffer_function",
                'long':long,
                'lat':lat,
                'userId':userId,
            }
        )

    @sync_to_async
    def buffer_function(self,event):
        userLocation = Point(event["long"],event["lat"])
        buffer = userLocation.buffer(0.008)
        print(buffer)
        # # sync_to_async(self._update_rider(event["userId"],event["long"],event["lat"]))
        # Rider.objects.filter(user_id =event["userId"]).update(loc = Point(event["long"],event["lat"],srid=4326))

    async def disconnect(self, close_code):
        print(close_code)
        pass