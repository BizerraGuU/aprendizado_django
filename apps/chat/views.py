from django.http import HttpResponse
from django.shortcuts import render
from .models import Message, Room

#aqui é onde é feita a integração entre o front e o back end
#onde também é feita as requisições de ambos os 'ends'

def home(request):

    messages = Message.objects.all()
    
    room = Room.objects.all()

    return render(request, 'chat/home.html', {
        'message': messages, 
        'room': room,
    })