from django.contrib import admin
from skills.views import home
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', home, name='home'),
] + [
    path('skills/', include('skills.urls')),
    path('exchange/', include('exchange.urls')),
    path('reviews/', include('reviews.urls')),
    path('reports/', include('reports.urls')),
    path('chat/', include('chat.urls')),
]