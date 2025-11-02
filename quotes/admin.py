from django.contrib import admin
from .models import Quote

# Register your models here.

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote_number', 'client', 'quote_date', 'quote_total')
    search_fields = ('quote_number', 'client__name')
    list_filter = ('quote_date',)
    list_per_page = 10
    list_display_links = ('quote_number', 'client', 'quote_date', 'quote_total')

admin.site.register(Quote, QuoteAdmin)
