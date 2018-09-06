from django.urls import path

from . import views

# Achtung, ab Django 2.0: in der app/urls.py app_name hinzufügen und in der zentralen urls.py nur ein include ('contact.urls')
# nichts mit namespace oder app_name in zentralen urls.py
app_name='contact'

urlpatterns = [
    path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
    ]