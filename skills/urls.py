from django.urls import path
from .views import create_skill, skill_list, update_skill, delete_skill

urlpatterns = [
    path('', skill_list, name='skill_list'),
    path('create/', create_skill, name='create_skill'),
    path('update/<int:pk>/', update_skill, name='update_skill'),
    path('delete/<int:pk>/', delete_skill, name='delete_skill'),
]