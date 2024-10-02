from django.urls import path
from .views import show_site

urlpatterns = [
    path('', show_site, name='show_site'),
]