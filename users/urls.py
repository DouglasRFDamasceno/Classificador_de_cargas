from django.urls.conf import path
from . import views

urlpatterns = [
    path('userRegister', views.userRegister, name='userRegister'),
    path('logout', views.logout, name='logout'),
]