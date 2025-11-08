import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        # Called on connection.
        # To accept the connection call:
        print("conexion establecida")
        self.accept()

    def disconnect(self, close_code):
        # Called when the socket closes
        print("conexion terminada")

    def receive(self, text_data=None, bytes_data=None):
        
        text_data_json = json.loads(text_data)
        print(text_data_json)
        
        # Called with either text_data or bytes_data for each frame
        # You can call:
        self.send(text_data=json.dumps({
            'message': text_data_json['message']
        }))
