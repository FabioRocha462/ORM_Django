from django.contrib import admin
from address.models import Address
# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = ['city', 'state']
    search_fields = ('city',)

admin.site.register(Address, AddressAdmin)