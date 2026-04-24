from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from exchange.models import ExchangeRequest

# ADD REVIEW
@login_required
def add_review(request, exchange_id):
    exchange = get_object_or_404(ExchangeRequest, id=exchange_id)

    # BUSINESS RULE: only allow review if accepted
    if exchange.status != 'accepted':
        return redirect('view_requests')

    # determine who is reviewing who
    if request.user == exchange.sender:
        reviewed_user = exchange.receiver
    elif request.user == exchange.receiver:
        reviewed_user = exchange.sender
    else:
        return redirect('view_requests')

    # prevent duplicate review
    existing = Review.objects.filter(
        reviewer=request.user,
        reviewed=reviewed_user
    ).first()

    if existing:
        return redirect('view_requests')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.reviewed = reviewed_user
            review.save()
            return redirect('view_requests')
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form})


# VIEW REVIEWS FOR A USER
def user_reviews(request, user_id):
    reviews = Review.objects.filter(reviewed__id=user_id)
    return render(request, 'user_reviews.html', {'reviews': reviews})

# Create your views here.
