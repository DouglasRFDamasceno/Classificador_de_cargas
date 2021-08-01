from django.shortcuts import redirect, render, get_object_or_404
from .models import Machine

def machineRegister(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['name']
            area = request.POST['area']
            production = request.POST['production']

            if not name.strip():
                print('O campo Nome não pode ficar em branco')
                return redirect('machineRegister')

            if not area.strip():
                print('O campo Área não pode ficar em branco')
                return redirect('machineRegister')

            if not production.strip():
                print('O campo Produção não pode ficar em branco')
                return redirect('machineRegister')

            machine = Machine.objects.create(name=name, area=area, production=production)
            machine.save()

            print('Máquina criada com sucesso!')
            return redirect('machineList')
        else:
            return render(request, 'machines/machineRegister.html')
    else:
        return redirect('/')
        
def machineList(request):
    if request.user.is_authenticated:
        machinesDB = Machine.objects.all()

        dados = {
            'machines': machinesDB
        }

        return render(request, 'machines/machineList.html', dados)
    else:
        return redirect('/')

def updateMachine(request, machine_id_update):
    if request.user.is_authenticated:
        if request.POST: 
            name = request.POST['name']
            area = request.POST['area']
            production = request.POST['production']

            if not name.strip():
                print('O campo Nome não pode ficar em branco')
                return redirect('machineList')

            if not area.strip():
                print('O campo Área não pode ficar em branco')
                return redirect('machineList')

            if not production.strip():
                print('O campo Produção não pode ficar em branco')
                return redirect('machineList')

            machine = get_object_or_404(Machine, pk=machine_id_update)
            machine.name = name
            machine.area = area
            machine.production = production

            machine.save(update_fields=['name', 'area', 'production'])

            machinesDB = Machine.objects.all()

            print(machinesDB)
            dados = {
                'machines': machinesDB
            }

            return render(request, 'machines/machineList.html', dados)

        else:
            machine = get_object_or_404(Machine, pk=machine_id_update)

            dados = {
                'machine': machine
            }

            return render(request, 'machines/machineUpdate.html', dados)

    else:
        return redirect('/')

def deleteMachine (request, machine_id_delete):
    if request.user.is_authenticated:
        machine = get_object_or_404(Machine, pk=machine_id_delete)

        machine.delete()

        machinesDB = Machine.objects.all()

        print(machinesDB)
        dados = {
            'machines': machinesDB
        }

        return render(request, 'machines/machineList.html', dados)

    else:
        return redirect('/')