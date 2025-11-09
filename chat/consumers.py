from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync
from .models import RoomsModel


class ChatConsumer(JsonWebsocketConsumer):

    def connect(self):
        # antes de aceptar la conexion debo saber el nombre del grupo al cual conectarme
        # usare su id con el nombre chat antepuesto (ej: chat_1)
    
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_name = RoomsModel.objects.get(pk=self.room_id).name
        self.group_name = f"chat_{self.room_name}"
        
        self.agregar_grupo = async_to_sync(self.channel_layer.group_add)
        self.agregar_grupo(self.group_name, self.channel_name)

        # acepta la conexion a un websocket
        self.accept()
        print("Conexion aceptada en la sala: ", self.room_name)

    def disconnect(self, code):
        # cuando se desconecta de un websocket
        self.quitar_grupo = async_to_sync(self.channel_layer.group_discard)
        self.quitar_grupo(self.group_name, self.channel_name)
        print(f"Conexion de la sala {self.room_name} terminada.")


    def receive_json(self, content):

        mensaje = content.get('message') # mensaje recivido del cliente que debo enviar al grupo

        print("mensaje recivido--------", mensaje)

        self.enviar_grupo = async_to_sync(self.channel_layer.group_send)
        self.enviar_grupo(self.group_name, {
            "type": "chat.message",
            "message": mensaje,
            "username": self.scope['user'].get_username(),
            "room_name": self.room_name,
        })


    def chat_message(self, event):

        print("mensaje enviado a los grupos------")

        self.send_json(
            {
                "message": event['message'],
                "username": event['username'],
                "room_name": event['room_name']
            }
        )



