from django.shortcuts import render, redirect, get_object_or_404
from cliente.forms import ClienteForm
from cliente.models import Cliente

# Create your views here.

def principal(request):
    return render(request, 'main.html')


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Cliente cadastrado com sucesso!'
            data = {'form': form, 'msg': msg}
            return redirect('principal')
        else:
            msg = 'Por favro, corrija os erros abaixo'
            data = {'form': form, 'msg': msg}
    else:
        form = ClienteForm()
        msg = ''
        data = {'form': form, 'msg': msg}
    return render(request, 'cadastrar_cliente.html', data)
    

def consultar_cliente(request):
    consulta = request.GET.get('buscar', '')
    if consulta:
        clientes = Cliente.objects.filter(nome__icontains=consulta)
    else:
        clientes = Cliente.objects.all()
    data = {'clientes': clientes}
    return render(request, 'consultar_cliente.html', data)

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            msg = 'Cliente atualizado com sucesso!'
            data = {'form': form, 'msg': msg}
            return redirect('consultar')
        else:
            msg = 'Por favor, corrija os erros abaixo'
            data = {'form': form, 'msg': msg}
    else:
        form = ClienteForm(instance=cliente)
        msg = ''
        data = {'form': form, 'msg': msg}
    return render(request, 'cadastrar_cliente.html', data)
