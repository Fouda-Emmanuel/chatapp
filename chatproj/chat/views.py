from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.
def HomePage(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        room = request.POST['room']

        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name = room, username = user_name)
            
        except Room.DoesNotExist:
            create_room = Room(room_name=room)
            create_room.save()
            return redirect('room', room_name = room, username = user_name)

    return render(request, 'index.html')


def MessageView(request, room_name, username):
    get_room = Room.objects.get(room_name=room_name)
    if request.method == 'POST':
        message = request.POST['message']
        new_message = Message(room=get_room, sender=username, message=message)
        new_message.save( )
    get_message = Message.objects.filter(room=get_room)

    context = {
        'messages': get_message,
        'user': username
    }
    
    return render(request, 'message.html', context)