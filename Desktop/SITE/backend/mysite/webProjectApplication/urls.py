from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('reg/', views.RegisterUserView.as_view(), name='register_page'),
    path('terms/',views.terms),
    path('login/', views.ProjectLogin.as_view(), name='login_page'),
    path('logout/', views.ProjectLogout.as_view(), name='logout_page'),
    path('messenger/', views.messenger, name='messenger'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 