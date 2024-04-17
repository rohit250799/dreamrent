from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('hello/',views.hello_reader, name="hello_reader"),
    path('helloview/', views.HelloView.as_view(), name='hello'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.user_logout, name='logout'),
]