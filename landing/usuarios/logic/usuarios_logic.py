
from ..models import Usuario

def crear_usuario(pnombre, pemail):
    usuario_nuevo = Usuario(nombre=pnombre, email=pemail)
    usuario_nuevo.save()

