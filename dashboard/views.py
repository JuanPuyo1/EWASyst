from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from invoices.models import InvoiceForItem, InvoiceForMaintenance, InvoiceForStone, InvoiceForCustomized
# Create your views here.

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        # Count all types of invoices
        total_invoices = (
            InvoiceForItem.objects.count() +
            InvoiceForMaintenance.objects.count() +
            InvoiceForStone.objects.count() +
            InvoiceForCustomized.objects.count()
        )

        context = {
            'title': 'Dashboard',
            'user': request.user,
            'total_invoices': total_invoices,
        }

        return render(request, 'dashboard/dashboard.html', context)
    


   

