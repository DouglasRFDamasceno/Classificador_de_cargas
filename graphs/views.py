from django.shortcuts import redirect, render
from machines.models import Machine
from django.contrib import auth

def dataGraphs(request):
    if request.user.is_authenticated:
        machinesDB = Machine.objects.order_by('name').all()
        data = []
        labels = []

        for machine in machinesDB:
            data.append(machine.consumption)
            labels.append(machine.name)

        datas = {
            'machines': machinesDB,
            'labels': labels,
            'data': data
        }

        return render(request, 'graphs.html', datas)
    else:
        return redirect('/')