from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project
# Create your views here.

projectsList = [

            {'id': '1', 'title': 'Ecommerce Website', 'description': 'Fully functional ecommerce website' },

            { 'id': '2', 'title': 'Portfolio Website', 'description': 'A personal website to write articles and display work' },

            {'id': '3', 'title': 'Social Network', 'description': 'An open source project built by the community' }

]

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects,}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()        
    return render(request, 'projects/single-project.html', {'projectobj':projectObj, 'tags':tags})

