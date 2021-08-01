from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include('classifier.urls')),
    path('users/', include('users.urls')),
    path('machines/', include('machines.urls')),
    path('tables/', include('tables.urls')),
    path('admin/', admin.site.urls),
]
