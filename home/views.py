from django.shortcuts import render
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,"about.html")

def about(request):
    return render(request,"about.html")

def experience(request):
    return render(request,"experience.html")

def education(request):
    return render(request,"education.html")

def skills(request):
    return render(request,"skills.html")

def expertise(request):
    return render(request,"expertise.html")

def projects(request):
    return render(request,"projects.html")

def contact(request):
    return render(request,"contact.html")