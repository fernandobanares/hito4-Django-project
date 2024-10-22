from django.db import models
import uuid

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.TextField()  # Cambiado de URLField a TextField
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.customer_name