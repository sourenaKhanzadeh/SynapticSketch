# diagrams/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DiagramConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.diagram_id = self.scope['url_route']['kwargs']['diagram_id']
        self.group_name = f"diagram_{self.diagram_id}"

        # Join the group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # text_data could be JSON with the updated shape positions, etc.
        data = json.loads(text_data)
        # Broadcast to group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'diagram_message',
                'data': data
            }
        )

    async def diagram_message(self, event):
        await self.send(text_data=json.dumps(event['data']))
