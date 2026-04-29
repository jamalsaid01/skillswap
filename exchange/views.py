from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ExchangeRequest
from .forms import ExchangeRequestForm

# SEND REQUEST
@login_required
def send_request(request):
    if request.method == 'POST':
        form = ExchangeRequestForm(request.POST)
        if form.is_valid():
            exchange = form.save(commit=False)

            # BUSINESS RULE: cannot send to yourself
            if exchange.receiver == request.user:
                form.add_error(None, "You cannot send request to yourself")
            else:
                exchange.sender = request.user
                exchange.save()
                return redirect('view_requests')
    else:
        form = ExchangeRequestForm()

    return render(request, 'send_request.html', {'form': form})


# VIEW REQUESTS
@login_required
def view_requests(request):
    received = ExchangeRequest.objects.filter(receiver=request.user)
    sent = ExchangeRequest.objects.filter(sender=request.user)

    return render(request, 'view_requests.html', {
        'received': received,
        'sent': sent
    })


# ACCEPT REQUEST
@login_required
def accept_request(request, pk):
    exchange = get_object_or_404(ExchangeRequest, pk=pk, receiver=request.user)
    exchange.status = 'accepted'
    exchange.save()
    return redirect('view_requests')


# REJECT REQUEST
@login_required
def reject_request(request, pk):
    exchange = get_object_or_404(ExchangeRequest, pk=pk, receiver=request.user)
    exchange.status = 'rejected'
    exchange.save()
    return redirect('view_requests')


# Create your views here.
