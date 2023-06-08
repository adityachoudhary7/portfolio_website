
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.about,name='about'),
    path('about',views.about,name='about'),
    path('experience',views.experience,name='experience'),
    path('education',views.education,name='education'),
    path('skills',views.skills,name='skills'),
    path('expertise',views.expertise,name='expertise'),
    path('projects',views.projects,name='projects'),
    path('contact',views.contact,name='contact')





]
