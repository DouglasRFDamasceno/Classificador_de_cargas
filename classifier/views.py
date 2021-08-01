from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from machines.models import Machine
from django.contrib import auth

def index(request):
    if request.user.is_authenticated:
        consumptionTotal = 0
        machinesDB = Machine.objects.order_by('name').all()
        data = []
        labels = []

        for machine in machinesDB:
            consumptionTotal = consumptionTotal + int(machine.consumption)
            data.append(machine.consumption)
            labels.append(machine.name)

        print(labels)
        dados = {
            'machines': machinesDB,
            'consumptionTotal': consumptionTotal,
            'labels': labels,
            'data': data
        }

        return render(request, 'index.html', dados)
    else:
        return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == "" or password == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(username=username).exists():
            # username = User.objects.filter(username).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('index')
        return redirect('/')

    return render(request, 'users/login.html')