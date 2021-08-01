from django.urls.conf import path
from . import views

urlpatterns = [
    path('graphs', views.dataGraphs, name='graphs'),
]