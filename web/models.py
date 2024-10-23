from django.db import models
import uuid
from django.contrib.auth.models import User

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=500)  
    is_private = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class Contact(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.customer_name

class Comentario(models.Model):
    flan = models.ForeignKey(Flan, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username}: {self.texto[:20]}"
