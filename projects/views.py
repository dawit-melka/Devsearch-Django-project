from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib import messages
from .models import Project, Tag
from .forms import ProjectForm
from .utils import searchProjects
# Create your views here.



def projects(request):
    projects, search_query = searchProjects(request)
    
    context = {'projects':projects, 'search_query':search_query}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'projectobj':projectObj,})

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form  = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, 'Project was created')
            return redirect('account')
        
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form  = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project was updated')
            return redirect('account')
        
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.info(request, 'Project was deleted')
        return redirect('account')
    context = {'object':project}
    return render(request, 'delete_template.html', context)

