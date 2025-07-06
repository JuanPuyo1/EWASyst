from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from invoices.models import Invoice
from clients.models import Client
from quotes.models import Quote
from inventories.models import Inventory
from django.db.models import Sum
import plotly.graph_objects as go
import plotly.offline as opy
from django.utils import timezone
from django.db.models.functions import TruncMonth
from django.db.models import Count

# Create your views here.

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        # Count all types of clients
        total_clients = (
            Client.objects.count()
        )

        # Count all types of quotes
        total_quotes = (
            Quote.objects.count()
        )

        # Count all types of invoices
        total_invoices = (
            Invoice.objects.count()
        )

        # Count all types of inventory
        try:
            total_inventory = Inventory.objects.aggregate(Sum('price'))['price__sum']
        except:
            total_inventory = 0

        # Recent items (last 5)
        recent_quotes = Quote.objects.select_related('client').order_by('-quote_date')[:5]
        recent_invoices = Invoice.objects.select_related('client').order_by('-created_at')[:5]
        recent_clients = Client.objects.order_by('-created_at')[:5]
        
        # Low stock alerts (items with stock <= 5)
        low_stock_items = Inventory.objects.filter(stock__lte=5).order_by('stock')[:5]

        # Quotes vs Invoices Over Time
        quote_counts = (
            Quote.objects
            .values('quote_date')
            .annotate(count=Count('id'))
            .order_by('quote_date')
        )
        invoice_counts = (
            Invoice.objects
            .annotate(month=TruncMonth('created_at'))
            .values('month')
            .annotate(count=Count('id'))
            .order_by('month')
        )

        # Prepare data for Plotly
        quote_dates = [q['quote_date'] for q in quote_counts]
        quote_values = [q['count'] for q in quote_counts]
        invoice_dates = [i['month'] for i in invoice_counts]
        invoice_values = [i['count'] for i in invoice_counts]

        quotes_trace = go.Bar(x=quote_dates, y=quote_values, name='Quotes')
        invoices_trace = go.Bar(x=invoice_dates, y=invoice_values, name='Invoices')
        quotes_vs_invoices_fig = go.Figure(data=[quotes_trace, invoices_trace])
        quotes_vs_invoices_fig.update_layout(barmode='group', title='Cotizaciones vs Facturas sobre el tiempo')
        quotes_vs_invoices_div = opy.plot(quotes_vs_invoices_fig, auto_open=False, output_type='div')

        # Inventory Distribution (by name for now)
        inventory = Inventory.objects.values('name').annotate(total=Sum('price'))
        inventory_labels = [item['name'] for item in inventory]
        inventory_values = [item['total'] for item in inventory]
        inventory_fig = go.Figure(data=[go.Pie(labels=inventory_labels, values=inventory_values)])
        inventory_fig.update_layout(title='Distribución de Inventarios')
        inventory_div = opy.plot(inventory_fig, auto_open=False, output_type='div')

        # Revenue Trends
        revenue = (
            Invoice.objects
            .annotate(month=TruncMonth('invoice_date'))
            .values('month')
            .annotate(total=Sum('invoice_total'))
            .order_by('month')
        )
        revenue_dates = [r['month'] for r in revenue]
        revenue_values = [r['total'] for r in revenue]
        revenue_fig = go.Figure(data=[go.Scatter(x=revenue_dates, y=revenue_values, mode='lines+markers', name='Ingresos')])
        revenue_fig.update_layout(title='Tendencias de Ingresos')
        revenue_div = opy.plot(revenue_fig, auto_open=False, output_type='div')

        context = {
            'title': 'Dashboard',
            'user': request.user,
            'total_invoices': total_invoices,
            'total_inventory': total_inventory,
            'total_quotes': total_quotes,
            'total_clients': total_clients,
            'recent_quotes': recent_quotes,
            'recent_invoices': recent_invoices,
            'recent_clients': recent_clients,
            'low_stock_items': low_stock_items,
            'quotes_vs_invoices_div': quotes_vs_invoices_div,
            'inventory_div': inventory_div,
            'revenue_div': revenue_div,
        }

        return render(request, 'dashboard/dashboard.html', context)