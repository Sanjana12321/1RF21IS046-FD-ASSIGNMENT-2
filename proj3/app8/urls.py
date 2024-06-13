from django.urls import path
from . import views

urlpatterns = [
    path('decoded/', views.decode_message, name='decoded/'),
]