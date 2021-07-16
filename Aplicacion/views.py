import django_filters
from django.shortcuts import render, redirect


from Aplicacion.form import *
from Aplicacion.models import *
from django_filters.views import FilterView


def Aplicacion(request):
    return render(request, 'home.html')


def inicio(request):
    return render(request, 'home.html')


def listaClientes(request):
    datos = {'listaClientes': Cliente.objects.all()}
    return render(request, 'clientes.html', datos)


def agregarClientes(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('clientes')

    else:
        formulario = ClienteForm()

    datos = {'form': formulario}
    return render(request, 'agregarClientes.html', datos)


def listaPlanes(request):
    datos = {'listaPlanes': Plan_reciclaje.objects.all()}
    return render(request, 'planes.html', datos)


def agregarPlanes(request):
    if request.method == 'POST':
        formulario = PlanForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('planes')

    else:
        formulario = PlanForm

    datos = {'form': formulario}
    return render(request, 'agregarPlanes.html', datos)


def modificarClientes(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)

    if request.method == 'POST':
        formulario = ClienteForm(request.POST, instance=cliente)

        if formulario.is_valid():
            formulario.save()
            return redirect('clientes')

    else:
        formulario = ClienteForm(instance=cliente)

    datos = {'form': formulario}
    return render(request, 'modificarClientes.html', datos)


def eliminarClientes(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect('clientes')


def modificarPlanes(request, id_plan):
    planes = Plan_reciclaje.objects.get(id_plan=id_plan)

    if request.method == 'POST':
        formulario = PlanForm(request.POST, instance=planes)

        if formulario.is_valid():
            formulario.save()
            return redirect('planes')

    else:
        formulario = PlanForm(instance=planes)

    datos = {'form': formulario}
    return render(request, 'modificarPlanes.html', datos)


def eliminarPlanes(request, id_plan):
    planes = Plan_reciclaje.objects.get(id_plan=id_plan)
    planes.delete()
    return redirect('planes')


class filtroEntregas(django_filters.FilterSet):
    fecha_entrega = django_filters.DateFilter()

    fecha_entrega = django_filters.DateFilter(
        widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
            }
        )
    )


class listaEntregas(FilterView):
        model = Cliente
        template_name = 'entregas1.html'
        context_object_name = 'entregas'
        filterset_class = filtroEntregas
        widgets = {'fecha_entrega': DateInput(attrs={'type': 'date'})}

        class Meta:
            model = Cliente
            fields = ['fecha_entrega']










