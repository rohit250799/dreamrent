from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    #path('', views.testView, name='testing'),
]