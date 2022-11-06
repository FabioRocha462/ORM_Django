from django.contrib import admin
from client.models import Client
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','cpf']
    search_fields = ('name','cpf',)

admin.site.register(Client, ClientAdmin)
