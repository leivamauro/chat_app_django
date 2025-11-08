from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import RoomsModel

# Create your views here.
def home(request: HttpRequest):

    data = {
        'rooms': RoomsModel.objects.all()
    }
    return render(request=request, template_name='chat/home.html', context=data)


def room(request: HttpRequest, room_id: int):
    try:
        room = RoomsModel.objects.get(pk=room_id)
    except RoomsModel.DoesNotExist:
        return HttpResponse("la sala seleccionada no existe")

    data = {
        'room': room,
    }

    return render(request, 'chat/room.html', context=data)