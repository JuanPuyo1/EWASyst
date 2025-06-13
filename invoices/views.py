from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import InvoiceForItem, InvoiceForMaintenance, InvoiceForCustomized, JewelleryItem
from .forms import InvoiceForItemForm, InvoiceForCustomizedForm
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
# Create your views here.

#Generar PDF
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import os
from django.conf import settings
from reportlab.lib.utils import simpleSplit
# Create your views here.

class InvoicesListView(View):
    def get(self, request):
        invoices = []         
        filter_type = None

        if request.GET.get('invoice_type'):
            invoice_type = request.GET.get('invoice_type')
            if invoice_type == 'item':
                invoices = InvoiceForItem.objects.all()
                filter_type = "item"
            elif invoice_type == 'maintenance':
                invoices = InvoiceForMaintenance.objects.all()
                filter_type = "maintenance"
            elif invoice_type == 'customized':
                invoices = InvoiceForCustomized.objects.all()
                filter_type = "customized"

        context = {
            'invoices': invoices,
            'filter_type': filter_type
        }
        return render(request, 'invoices/invoices_list.html', context)

class InvoicesCreateOptionView(View):
    def get(self, request):
        return render(request, 'invoices/invoices_create_option.html')

class InvoicesConfirmDeleteView(View):
    template_name = 'invoices/invoices_confirm_delete.html'
    success_url = reverse_lazy('invoices:invoices_list')
    
    def get(self, request, *args, **kwargs):
        invoice = get_object_or_404(InvoiceForItem, pk=kwargs['pk'])

        if invoice:
            return render(request, self.template_name, {'invoice': invoice})
        else:
            invoice = get_object_or_404(InvoiceForMaintenance, pk=kwargs['pk'])
            if invoice:
                return render(request, self.template_name, {'invoice': invoice})
            else:
                invoice = get_object_or_404(InvoiceForCustomized, pk=kwargs['pk'])
                if invoice:
                    return render(request, self.template_name, {'invoice': invoice})
                else:
                    print("No se encontró la factura")
    
    def post(self, request, *args, **kwargs):
        invoice = get_object_or_404(InvoiceForItem, pk=kwargs['pk'])
        if invoice:
            invoice.delete()
            return redirect(self.success_url)
        else:
            invoice = get_object_or_404(InvoiceForMaintenance, pk=kwargs['pk'])
            if invoice:
                invoice.delete()
                return redirect(self.success_url)
            else:
                invoice = get_object_or_404(InvoiceForCustomized, pk=kwargs['pk'])
                if invoice:
                    invoice.delete()
                    return redirect(self.success_url)
                else:
                    print("No se encontró la factura")
                    return redirect(self.success_url)

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

def generate_pdf_item(request, invoice_id):
    BASE_DIR = settings.BASE_DIR
    # Create buffer and canvas
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    
    # Get quote data
    invoice = InvoiceForItem.objects.get(id=invoice_id)
    
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
    for item in invoice.items.all():
        # Split description into lines that fit within 220 points width
        description_lines = simpleSplit(item.jewellery_name, p._fontname, p._fontsize, 220)
        
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
    p.drawString(50, y_position - 20, invoice.observation)
    
    # Footer
    y_position = 150  # Adjust this value as needed
    
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



class InvoicesCreateForCustomizedView(View):
    def get(self, request):
        initial_data = request.session.pop('invoice_initial_data', None)
        if initial_data:
            form = InvoiceForCustomizedForm(initial=initial_data)
        else:
            form = InvoiceForCustomizedForm()
    
        request.session['invoice_initial_data'] = None
        return render(request, 'invoices/invoices_create_custom.html', {'form': form})

    def post(self, request):
        print(request.POST)
        form = InvoiceForCustomizedForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            invoice = InvoiceForCustomized.objects.create(
                client=form.cleaned_data['client'],
                invoice_number=form.cleaned_data['invoice_number'],
                invoice_type=form.cleaned_data['invoice_type'],
                invoice_date=form.cleaned_data['invoice_date'],
                invoice_status=form.cleaned_data['invoice_status'],
                description=form.cleaned_data['description'],
                observation=form.cleaned_data['observation'],
                invoice_total=form.cleaned_data['invoice_total'],
                invoice_balance=form.cleaned_data['invoice_balance']
            )
            invoice.save()

            return redirect('invoices:invoices_list')
        else:
            print(form.errors)
            return redirect('invoices:invoices_create_for_customized')

def invoices_delete(request, pk):
    invoice = get_object_or_404(InvoiceForItem, pk=pk)
    if invoice:
        invoice.delete()
    else:
        invoice = get_object_or_404(InvoiceForMaintenance, pk=pk)
        if invoice:
            invoice.delete()
        else:
            return redirect('invoices:invoices_list')
    return redirect('invoices:invoices_list')



