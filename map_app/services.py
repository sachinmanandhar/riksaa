import json

class RiderInfoService:

    async def get_rider_position_within_buffer(self, text_data):
        
        datapoint = json.loads(text_data)

        long = datapoint['long']
        lat = datapoint['lat']
        userId = datapoint['user']
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'long':long,
                'lat':lat,
                'userId':userId
            }
        )