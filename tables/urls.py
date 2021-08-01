from django.urls.conf import path
from . import views

urlpatterns = [
    path('tables', views.dataTables, name='tables'),
]