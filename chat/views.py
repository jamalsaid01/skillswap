from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from exchange.models import ExchangeRequest

@login_required
def chat_room(request, exchange_id):
    exchange = get_object_or_404(ExchangeRequest, id=exchange_id)

    # get all messages for this exchange
    messages = Message.objects.filter(exchange=exchange).order_by('created_at')

    if request.method == 'POST':
        text = request.POST.get('text')

        if text:
            Message.objects.create(
                exchange=exchange,
                sender=request.user,
                text=text
            )
            return redirect('chat_room', exchange_id=exchange.id)

    return render(request, 'chat_room.html', {
        'exchange': exchange,
        'messages': messages
    })

# Create your views here.
