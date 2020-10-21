from User.models import auth_user
from .models import Cliente

def CrearCliente(cod_user, empresa, ruc, direccion):
    usr = auth_user.objects.get(id=cod_user)
    new_clie = Cliente(usuario=usr, empresa=empresa, ruc=ruc, direccion=direccion)
    new_clie.save()
    new_clie.cod_cliente_publico = 'C' + str(new_clie.pk)
    new_clie.save()
    return 1
