from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from django.utils import timezone
from django.db.models import Q
from .models import Evento,EventoLocalidad,Reserva

def productosIndex(request):
    # Desactivar eventos cuya fecha ya pasó
    hoy = timezone.now()
    Evento.objects.filter(fecha__lt=hoy, activo=True).update(activo=False)

    # Obtener parámetros de búsqueda
    query = request.GET.get('q', '')
    tipo = request.GET.get('tipo', '')

    # Filtrar eventos activos
    eventos = Evento.objects.filter(activo=True)

    if query:
        eventos = eventos.filter(nombre__icontains=query)

    if tipo:
        eventos = eventos.filter(tipo__icontains=tipo)

    eventos = eventos.order_by('-fecha')

    # Paginación
    paginator = Paginator(eventos, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Localidades
    eventos_Localidades = EventoLocalidad.objects.all()

    # Tipos disponibles para el filtro
    tipos = Evento.objects.values_list('tipo', flat=True).distinct()

    # Renderizar plantilla
    template = loader.get_template("eventos.html")
    context = {
        "page_obj": page_obj,
        "eventos": eventos,
        "Localidad": eventos_Localidades,
        "tipos": tipos,
        "query": query,
        "tipo_selected": tipo
    }

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