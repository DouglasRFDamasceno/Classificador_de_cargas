from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

def userRegister(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            firstName = request.POST['firstName']
            lastName = request.POST['lastName']
            email = request.POST['email']
            userName = request.POST['userName']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if not firstName.strip():
                print('O campo Nome não pode ficar em branco')
                return redirect('userRegister')

            if not lastName.strip():
                print('O campo Sobrenome não pode ficar em branco')
                return redirect('userRegister')

            if not email.strip():
                print('O campo email não pode ficar em branco')
                return redirect('userRegister')

            if not userName.strip():
                print('O campo Login não pode ficar em branco')
                return redirect('userRegister')

            if password1 != password2:
                print('As senhas não são iguais')
                return redirect('userRegister')

            if User.objects.filter(username=userName).exists():
                print('Usuário já cadastrado')
                return redirect('userRegister')

            user = User.objects.create_user(first_name=firstName, last_name=lastName, username=userName, email=email, password=password1)
            user.save()
            print('Usuário criado com sucesso!')
            return redirect('index')
        else:
            return render(request, 'users/userRegister.html')
    else:
        return redirect('/')
        
def logout(request):
    auth.logout(request)
    return redirect('/')
