from django.views.generic import DetailView
from Cliente.models import Cliente
import json
import os
from django.http import HttpResponse


class Files(DetailView):
    context_object_name = 'usuario'
    model = Cliente
    template_name = 'files/files.html'


def filtrarCertificados(request):
    if request.is_ajax:
        texto = request.GET['texto']
        cod_cliente = Cliente.objects.get(usuario=request.user).cod_cliente
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'certificados.json')
        data_json = open(file_path)
        certificados = json.load(data_json)
        filtrados = [x for x in certificados if texto in x['numero'] or texto.lower() in x['serie'].lower()]
        data = json.dumps(filtrados)
        mimetype = "application/json"
        return HttpResponse(data, mimetype)



