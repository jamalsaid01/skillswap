from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()

    context = {
        "name": "Mwalimu Said Bhahati",
        "role": "Junior Backend Developer",
        "location": "Mombasa, Kenya",
        "email": "mwalimubhahati@gmail.com",
        "github": "https://github.com/jamalsaid01",
        "about": "Dedicated Junior Backend Developer trained at Swahili Pot Hub, focused on building backend systems using Django, Python, and SQL.",
        "projects": projects
    }

    return render(request, "core/index.html", context)

# Create your views here.
