from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

''' 
from django.contrib.auth.models import User - importa do admin o user 

'''


def login(request):
    form = LoginForms()
    ''' 
    confirma as informações de cadastro e faz login  

    '''
    if request.method == 'POST':
        form = LoginForms(request.POST)
        # Verifica se o formulário é valido 
        if form.is_valid:
            nome=form['nome_login'].value()
            senha=form['senha'].value()
        
        # verifica se o login está no banco de dados 
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None: 
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')


    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    ''' 
    Criando um novo formulário com as informações na url de cadastro 

    '''
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        # Verifica se o formulário é valido 
        if form.is_valid():
                       
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            #verifica se o nome de usuário já existe e aplica mensagem de erro caso exista 
            if  User.objects.filter(username=nome).exists():
                messages.error(request,'Usuário já existente')
                return redirect('cadastro')

            #Cria o usuário e mostra mensagem de sucesso caso cadastrado 
            usuario = User.objects.create_user(
                username=nome, 
                email= email, 
                password= senha
            )
            usuario.save()
            messages.success(request,' Cadastro efetuado com sucesso')
            return redirect('login')
    return render(request, "usuarios/cadastro.html", {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')