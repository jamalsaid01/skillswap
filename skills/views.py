from django.shortcuts import render, redirect, get_object_or_404
from .models import Skill
from .forms import SkillForm
from django.contrib.auth.decorators import login_required

# CREATE
@login_required
def create_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('skill_list')
    else:
        form = SkillForm()

    return render(request, 'create_skill.html', {'form': form})


# READ (LIST)
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'skill_list.html', {'skills': skills})


# UPDATE
@login_required
def update_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm(instance=skill)

    return render(request, 'update_skill.html', {'form': form})


# DELETE
@login_required
def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)

    if request.method == 'POST':
        skill.delete()
        return redirect('skill_list')

    return render(request, 'delete_skill.html', {'skill': skill})

from django.db.models import Q

def skill_list(request):
    query = request.GET.get('q')

    if query:
        skills = Skill.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(skill_type__icontains=query)
        )
    else:
        skills = Skill.objects.all()

    return render(request, 'skill_list.html', {'skills': skills})

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# Create your views here.
