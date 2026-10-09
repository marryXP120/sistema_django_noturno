from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForma

# Create your views here.
@login_required
def index(request):
    pacientes = Paciente.objects.all()
    return render(request, "index.html", {'pacientes':pacientes})

@login_required
def novo_paciente(request):
    if request.method == 'POST':
       form = PacienteForme(request.'POST')
       if form.is_valid():
           form.save()
           return redirect(''novo_paciente_sucesso')
       else:
           form = pacienteForm()
    return render(request, "novo-paciente.html")

@login_required
def novo_paciente_sucesso(request):
    return render(request, "novo-paciente-sucesso.html")

@login_required
    def alterar_paciente(request,codigo_paciente)
    (codigo_paciente=codigo_paciente)
    if request.method == 'POST':
    form = PacienteForm(request.POST, instance=paciente)
    if form.is_valid()
    form.save()
    return redirect('index')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'alterar_dados.html',{
        'form':form,
        'paciente':paciente,
    })
        
    paciente = Paciente.objects.get(codigo_paciente=codigo_paciente)
    if request.method == 'POST':
        paciente.nome = request.POST.get('nome')
        paciente.cpf = request.POST.get('cpf')
        paciente.email = request.POST.get('email')
        paciente.telefone = request.POST.get('telefone')
        paciente.data_nascimento = request.POST.get('data_nascimento')

        paciente.save()

        return redirect('index')
    return render(request, "alterar_dados.html", {'paciente':paciente})


def buscar_pacient(request):
    query = request.GET.get('query')
    pacientes = Paciente.objects.filter(nome__icontains=query)
    return render(request, "index.html", {'pacientes': pacientes})
   
@login_required
def excluir_paciente(request, codigo_paciente):
    paciente = Paciente.objects.get(codigo_paciente=codigo_paciente)
    paciente.delete()
    if request.method == 'POST':
        paciente.delete()
        return redirect('index')
    return render(request, "excluir_paciente.html", {'paciente': paciente})