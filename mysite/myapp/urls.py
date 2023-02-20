from django.urls import path, include
from .views import CustomRegistrationView, CustomLoginView, CustomLogoutView
from .api_views import RegisterAPI, LoginAPI, PublisherView
from . import views


urlpatterns = [
    path('register/', CustomRegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('api/register/', RegisterAPI.as_view(), name='register_api'),
    path('api/login/', LoginAPI.as_view(), name='login_api'),
    path('', views.index, name='index'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    
    path('api/publishers', PublisherView.as_view(), name='publisher_api'),
]
