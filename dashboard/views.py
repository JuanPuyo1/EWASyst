from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from invoices.models import Invoice
# Create your views here.

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        # Count all types of invoices
        total_invoices = (
            Invoice.objects.count()
        )

        context = {
            'title': 'Dashboard',
            'user': request.user,
            'total_invoices': total_invoices,
        }

        return render(request, 'dashboard/dashboard.html', context)
    


   

