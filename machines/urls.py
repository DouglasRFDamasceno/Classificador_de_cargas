from django.urls.conf import path
from . import views

urlpatterns = [
    path('machineRegister', views.machineRegister, name='machineRegister'),
    path('machineList', views.machineList, name='machineList'),
    path('update/<int:machine_id_update>', views.updateMachine, name='update/updateMachine'),
    path('delete/<int:machine_id_delete>', views.deleteMachine, name='delete/deleteMachine'),
]