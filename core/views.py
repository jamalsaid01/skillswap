from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Project


def home(request):
    """
    Portfolio Home View
    - Ensures default project exists
    - Displays projects
    - Handles contact form submissions
    """

    # Ensure default project exists (clean + safe)
    Project.objects.get_or_create(
        title="SkillSwap",
        defaults={
            "description": "A web-based platform enabling peer-to-peer skill exchange within communities.",
            "tech_stack": "Python, Django, SQL, HTML/CSS",
            "github_link": "https://github.com/jamalsaid01/skillswap.git",
        },
    )

    projects = Project.objects.all()

    # Handle contact form
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and message:
            full_message = f"""
New Portfolio Contact Message

Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
            """

            send_mail(
                subject=f"Portfolio Contact - {name}",
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

        return redirect("home")

    context = {
        "name": "Mwalimu Said Bhahati",
        "role": "Junior Backend Developer",
        "location": "Mombasa, Kenya",
        "email": "mwalimubhahati@gmail.com",
        "github": "https://github.com/jamalsaid01",
        "about": (
            "Detail-oriented Junior Backend Developer trained at Swahili Pot Hub, "
            "specializing in building scalable, secure, and efficient backend systems "
            "using Python, Django, and SQL."
        ),
        "projects": projects,
    }

    return render(request, "core/index.html", context)
