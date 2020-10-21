from django.db import models


class Files(models.Model):
    cod_file = models.AutoField(primary_key=True, max_length=8)
    cod_cliente = models.ForeignKey('Cliente.Cliente', on_delete=models.CASCADE)
    tipo_inspeccion = models.CharField(max_length=250, null=True, blank=True)
    tipo_doc = models.CharField(max_length=250, null=True, blank=True)
    name_file = models.CharField(max_length=100, null=True, blank=True)
    url_file = models.CharField(max_length=150, null=True, blank=True)
    estado = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'files'
