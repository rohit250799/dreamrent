from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt import views as jwt_views
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    #path('test/', default_views.testView, name='testing'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-view-create'),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='modify'), 
    path('blogposts/<int:pk>/', views.BlogPostList.as_view(), name='listblogs'),    

]
