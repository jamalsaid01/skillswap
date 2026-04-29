from django.urls import path
from .views import chat_room

urlpatterns = [
    path('<int:exchange_id>/', chat_room, name='chat_room'),
]