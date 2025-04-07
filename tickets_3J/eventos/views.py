from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from datetime import datetime

#from .forms import ProductoForm
from .models import Evento,EventoLocalidad,Reserva

# Vista principal de Productos
def productosIndex(request):
    # Consultar eventos y localidades
    eventos = Evento.objects.all().order_by('id')  # Ordena por ID de forma ascendente
    eventos_Localidades = EventoLocalidad.objects.all()

    # Configurar paginación para mostrar 9 eventos por página
    paginator = Paginator(eventos, 9)

    # Obtener el número de página desde la solicitud GET
    page_number = request.GET.get('page', 1)  # Cambié el valor predeterminado de 0 a 1
    page_obj = paginator.get_page(page_number)

    # Obtener el template
    template = loader.get_template("eventos.html")

    # Agregar el contexto
    context = {"page_obj": page_obj, "eventos": eventos, "Localidad": eventos_Localidades}

    # Retornar respuesta HTTP
    return HttpResponse(template.render(context, request))

#Vista para ver detalles de un autor
def detalleProducto(request, id):
    #Consultar producto
    evento = Evento.objects.get(id=id)  # Cambié de Eventos a evento

    #Consultar datos de producto
    context = {'evento': evento}  # Asegúrate de usar 'evento' en minúsculas
    #Obtener el template
    template = loader.get_template("detalleEvento.html")

    return HttpResponse(template.render(context, request))


def eliminarBoleta(request,id):
    #Obtener el template
    template = loader.get_template("eliminarReserva.html")
    #Buscar el producto
    obj = get_object_or_404(Reserva, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('productosIndex')
    #Agregar el contexto
    context = {}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))