from django.urls import path
from . import views
from django.contrib.auth import views as default_views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('hello/',views.hello_reader, name="hello_reader"),
    path('helloview/', views.HelloView.as_view(), name='hello'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', default_views.LoginView.as_view(template_name='user_authentication/login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
]