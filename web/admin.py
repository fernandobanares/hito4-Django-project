from django.contrib import admin
from .models import Flan
from .models import Contact

admin.site.register(Flan)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'message') 
