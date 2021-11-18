


from django.http.response import HttpResponse
from .logic import usuarios_logic


def anadir_usuario(request):
    items = list(request.POST.items())
    nombre =""
    email=""
    for item in items:
        if(item[0]=="nombre"): nombre = item[1]
        if(item[0]=="email"): email = item[1]
    
    usuarios_logic.crear_usuario(nombre, email)
    return HttpResponse("Se ha creado el usuario con nombre"+nombre+" y correo "+email)