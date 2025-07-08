from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Invoice
from .forms import InvoiceForm
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

#Generar PDF
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import os
from django.conf import settings
from reportlab.lib.utils import simpleSplit
# Create your views here.

class InvoicesListView(LoginRequiredMixin, View):
    def get(self, request):
        invoices = Invoice.objects.all()

        # Calculate restante for each invoice and add it to the context
        for invoice in invoices:
            invoice.restante = invoice.invoice_total - invoice.invoice_balance

        context = { 
            'invoices': invoices,
        }
        return render(request, 'invoices/invoices_list.html', context)


class InvoicesConfirmDeleteView(LoginRequiredMixin, DeleteView):
    model = Invoice
    template_name = 'invoices/invoices_confirm_delete.html'
    success_url = reverse_lazy('invoices:invoices_list')

class InvoicesCreate(LoginRequiredMixin, View):
    def get(self, request):

        initial_data = request.session.pop('invoice_initial_data', None)
        if initial_data:
            form = InvoiceForm(initial=initial_data)
        else:
            form = InvoiceForm()
        context = {
            'form': form,
        }
        request.session['invoice_initial_data'] = None
        return render(request, 'invoices/invoices_create.html', context)

    def post(self, request):
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoices:invoices_list')
        else:
            print(form.errors)
            return redirect('invoices:invoices_create')
        

class InvoicesDetailView(LoginRequiredMixin, DetailView):
    model = Invoice
    template_name = 'invoices/invoices_detail.html'
    context_object_name = 'invoice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restante'] = context['invoice'].invoice_total - context['invoice'].invoice_balance
        return context




class InvoicesUpdate(LoginRequiredMixin, UpdateView):
    model = Invoice
    template_name = 'invoices/invoices_update.html'
    context_object_name = 'invoice'
    form_class = InvoiceForm

@login_required
def generate_pdf_item(request, invoice_id):
    BASE_DIR = settings.BASE_DIR
    # Create buffer and canvas
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    
    # Get quote data
    invoice = Invoice.objects.get(id=invoice_id)
    
    # Set font
    p.setFont("Helvetica", 10)
    
    # Draw logo
    logo_path = os.path.join(BASE_DIR, 'invoices', 'static', 'invoices', 'logo.png') 
    p.drawImage(logo_path, 250, 700, width=100, height=100)
    
    # Draw company name
    p.setFont("Helvetica", 14)
    p.drawString(250, 680, "EWA JOYERÍA")
    
    # Customer details section (left side)
    p.setFont("Helvetica", 10)
    p.drawString(50, 600, "EMITIDO A:")
    p.drawString(50, 580, f"{invoice.client.name}")
    p.drawString(50, 560, f"{invoice.client.email}")
    p.drawString(50, 540, f"{invoice.client.phone}")
    
    # Quote details (right side)
    p.drawString(450, 600, "FACTURA")
    p.drawString(450, 580, f"FECHA: {invoice.invoice_date.strftime('%d.%m.%Y')}")
    p.drawString(450, 560, f"ID: {invoice.invoice_number}")
    
        # Table headers
    y_position = 480
    p.setFillColorRGB(0.9, 0.9, 0.9)  # Light gray background
    p.rect(50, y_position, 500, 20, fill=True)
    p.setFillColorRGB(0, 0, 0)  # Back to black text
    p.drawString(60, y_position + 5, "DESCRIPCIÓN")
    p.drawString(300, y_position + 5, "VALOR")
    p.drawString(400, y_position + 5, "QTY")
    p.drawString(480, y_position + 5, "TOTAL")
    
    # Items content
    y_position -= 30
    start_y = y_position  # Remember starting position
    
    # Process each item description
    description_lines = simpleSplit(invoice.observation, p._fontname, p._fontsize, 220)
    
        
        # Draw each line of the description
    for line in description_lines:
        p.drawString(60, y_position, line)
        y_position -= 15  # Move down 15 points for next line
        
        # Add some spacing between items
        y_position -= 10
        
        # Check if we need a new page
        if y_position < 200:  # Adjust this value based on your needs
            p.showPage()
            p.setFont("Helvetica", 10)
            y_position = 750  # Reset to top of new page
    
    # Draw the value, qty, and abono (aligned with first item)
    p.drawString(300, start_y, f"COP {invoice.invoice_total:,.0f}")
    p.drawString(400, start_y, "1")
    p.drawString(480, start_y, f"COP {invoice.invoice_total:,.0f}")
    
    # Adjust y_position for the total section
    y_position -= 20
    
    # Draw total section - create three rows
    row_height = 20
    
    # Total row
    p.setFillColorRGB(0.9, 0.9, 0.9)
    p.rect(50, y_position, 500, row_height, fill=True)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(400, y_position + 5, "TOTAL")
    p.drawString(480, y_position + 5, f"COP {invoice.invoice_total:,.0f}")
    
    # Abono row
    y_position -= row_height
    p.setFillColorRGB(0.9, 0.9, 0.9)
    p.rect(50, y_position, 500, row_height, fill=True)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(400, y_position + 5, "ABONO")
    p.drawString(480, y_position + 5, f"COP {invoice.invoice_balance:,.0f}")
    
    # Restante row
    y_position -= row_height
    p.setFillColorRGB(0.9, 0.9, 0.9)
    p.rect(50, y_position, 500, row_height, fill=True)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(400, y_position + 5, "RESTANTE")
    p.drawString(480, y_position + 5, f"COP {invoice.invoice_total - invoice.invoice_balance:,.0f}")
    
    # Notes section
    y_position -= 40
    p.drawString(50, y_position, "Notas:")

    additional_notes_lines = simpleSplit(invoice.additional_notes, p._fontname, p._fontsize, 220)
    y_position -= 15
    for line in additional_notes_lines:
        p.drawString(50, y_position, line)
        y_position -= 10
    
    

    # Footer
    y_position = 120  # Adjust this value as needed
    
    # DETALLES section (left side)

    p.drawString(50, y_position, "DETALLES")
    p.drawString(50, y_position - 20, "Métodos de pago:")
    p.drawString(50, y_position - 35, "Daviplata-Nequi: 3105458202")
    p.drawString(50, y_position - 50, "Cuenta de Ahorros Davivienda:")
    p.drawString(50, y_position - 65, "457900065071")
    p.drawString(50, y_position - 80, "Para más información puede")
    p.drawString(50, y_position - 95, "contactarnos aquí")
    
    # GRACIAS and signature (right side)
    p.drawString(450, y_position, "GRACIAS")
    
    # Draw signature
    sign_path = os.path.join(BASE_DIR, 'quotes', 'static', 'quotes', 'sign.jpg')
    p.drawImage(sign_path, 400, y_position - 100, width=150, height=80)  # Adjust width/height as needed
    
    # Close the PDF object
    p.showPage()
    p.save()
    
    # FileResponse
    buffer.seek(0)

    response = FileResponse(buffer, content_type="application/pdf")
    response["Content-Disposition"] = "inline; filename={}".format(f"factura_{invoice.id}.pdf")
    return response





