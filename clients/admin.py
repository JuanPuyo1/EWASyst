from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'document_type', 'document_number')
    search_fields = ('name', 'email', 'phone', 'document_type', 'document_number')
    list_filter = ('document_type',)
    list_per_page = 10
    list_display_links = ('name', 'email', 'phone', 'document_type', 'document_number')

admin.site.register(Client, ClientAdmin)
 

