from django.shortcuts import render

# Create your views here.
from .models import ContactInformation, Education, Experience, Project, Skill

def cv(request):
    contact = ContactInformation.objects.first() 
    educations = Education.objects.all() 
    experiences = Experience.objects.all() 
    projects = Project.objects.all() 
    skills = Skill.objects.all() 

    context = {
        'contact': contact,
        'educations': educations,
        'experiences': experiences,
        'projects': projects,
        'skills': skills
    } 

    return render(request, 'cv_app/cv_template.html', context) 

def home(request):
    contact = ContactInformation.objects.first() 
    return render(request, 'cv_app/index.html', {'contact': contact}) 