from django.shortcuts import render, redirect
from django.views import View
from .models import InvoiceForItem, InvoiceForMaintenance, JewelleryItem
from .forms import InvoiceForItemForm
# Create your views here.

class InvoicesListView(View):
    def get(self, request):
        invoices = InvoiceForItem.objects.all()
        invoices_maintenance = InvoiceForMaintenance.objects.all()
        context = {
            'invoices': invoices,
            'invoices_maintenance': invoices_maintenance
        }
        return render(request, 'invoices/invoices_list.html', context)

class InvoicesCreateListView(View):
    def get(self, request):
        return render(request, 'invoices/invoices_create_option.html')

class InvoicesCreateForItemView(View):
    def get(self, request):

        initial_data = request.session.pop('invoice_initial_data', None)
        if initial_data:
            form = InvoiceForItemForm(initial=initial_data)
        else:
            form = InvoiceForItemForm()
        items = JewelleryItem.objects.all()
        context = {
            'form': form,
            'items': items
        }
        request.session['invoice_initial_data'] = None
        return render(request, 'invoices/invoices_create.html', context)

    def post(self, request):
        form = InvoiceForItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoices:invoices_list')

