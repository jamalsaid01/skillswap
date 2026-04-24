from django.shortcuts import render
from django.contrib.auth.models import User
from skills.models import Skill
from exchange.models import ExchangeRequest
from reviews.models import Review
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

@login_required
def report_view(request):
    # TOTAL COUNTS
    total_users = User.objects.count()
    total_skills = Skill.objects.count()
    total_exchanges = ExchangeRequest.objects.count()
    accepted_exchanges = ExchangeRequest.objects.filter(status='accepted').count()

    # TOP RATED USERS
    top_users = User.objects.annotate(
        avg_rating=Avg('received_reviews__rating')
    ).order_by('-avg_rating')[:5]

    context = {
        'total_users': total_users,
        'total_skills': total_skills,
        'total_exchanges': total_exchanges,
        'accepted_exchanges': accepted_exchanges,
        'top_users': top_users
    }

    return render(request, 'report.html', context)

# Create your views here.
