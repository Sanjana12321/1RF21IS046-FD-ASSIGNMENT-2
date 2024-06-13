from django.urls import path
from . import views

urlpatterns = [
    path('', views.converted, name='converted'),
    path('cheque_print/', views.cheque_print, name='cheque_print'),
]