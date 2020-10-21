from django.db import models

class Cliente(models.Model):
    cod_cliente = models.AutoField(primary_key=True, max_length=7)
    usuario = models.OneToOneField('User.auth_user', on_delete=models.CASCADE)
    empresa = models.CharField(max_length=120, null=True, blank=True)
    ruc = models.CharField(max_length=11, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    cod_publico = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'cliente'
        managed = True