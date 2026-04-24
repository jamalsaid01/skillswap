from django.urls import path
from .views import add_review, user_reviews

urlpatterns = [
    path('add/<int:exchange_id>/', add_review, name='add_review'),
    path('user/<int:user_id>/', user_reviews, name='user_reviews'),
]