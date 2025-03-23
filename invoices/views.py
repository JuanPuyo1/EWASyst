from django.shortcuts import render
from django.views import View
from .models import InvoiceForItem, InvoiceForMaintenance
# Create your views here.

class InvoicesListView(View):
    def get(self, request):
        invoices = InvoiceForItem.objects.all()
        invoices_maintenance = InvoiceForMaintenance.objects.all()
        context = {
            'invoices': invoices,
            'invoices_maintenance': invoices_maintenance
        }
        return render(request, 'invoices/invoice_list.html', context)
