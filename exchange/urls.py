from django.urls import path
from .views import send_request, view_requests, accept_request, reject_request

urlpatterns = [
    path('send/', send_request, name='send_request'),
    path('', view_requests, name='view_requests'),
    path('accept/<int:pk>/', accept_request, name='accept_request'),
    path('reject/<int:pk>/', reject_request, name='reject_request'),
]