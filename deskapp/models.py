from django.db import models

# Create your models here.
class Session(models.Model):
    name = models.CharField(max_length =100, unique=True)
    pwd = models.CharField(max_length=10, unique=True)
    created_at= models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name="Inicio"
        verbose_name_plural="Inicios"
        ordering =['-created_at']

    def __str__(self):
        return self.name