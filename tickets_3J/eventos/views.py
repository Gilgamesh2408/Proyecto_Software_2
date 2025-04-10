from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from django.utils import timezone
#from .forms import ProductoForm
from .models import Evento,EventoLocalidad,Reserva

def productosIndex(request):
    # Desactivar eventos cuya fecha ya pasó
    hoy = timezone.now()
    Evento.objects.filter(fecha__lt=hoy, activo=True).update(activo=False)

    # Obtener solo eventos activos y ordenarlos por fecha descendente
    eventos = Evento.objects.filter(activo=True).order_by('-fecha')

    # Obtener todas las localidades
    eventos_Localidades = EventoLocalidad.objects.all()

    # Configurar paginación (9 eventos por página)
    paginator = Paginator(eventos, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Cargar template
    template = loader.get_template("eventos.html")

    # Contexto para la plantilla
    context = {
        "page_obj": page_obj,
        "eventos": eventos,
        "Localidad": eventos_Localidades
    }

    # Retornar respuesta
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