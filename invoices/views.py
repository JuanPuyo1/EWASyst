from django.shortcuts import render
from django.views import View
# Create your views here.
class InvoicesListView(View):
    def get(self, request):
        return render(request, 'invoices/invoices_list.html')
