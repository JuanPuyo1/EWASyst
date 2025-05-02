from django.shortcuts import render
from .models import Quote
from .forms import QuoteForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from invoices.models import InvoiceForItem
from invoices.forms import InvoiceForItemForm
from django.shortcuts import redirect

#Generar PDF
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import os
from django.conf import settings
from reportlab.lib.utils import simpleSplit
# Create your views here.

class QuoteView(ListView):
    model = Quote
    template_name = 'quote_list.html'
    context_object_name = 'quotes'

class QuoteCreateView(CreateView):
    model = Quote
    form_class = QuoteForm
    template_name = 'quotes/quote_create.html'
    success_url = reverse_lazy('quotes:quote_list')

class QuoteUpdateView(UpdateView):
    model = Quote
    form_class = QuoteForm
    template_name = 'quotes/quote_create.html'
    success_url = reverse_lazy('quotes:quote_list')

class QuoteDeleteView(DeleteView):
    model = Quote
    template_name = 'quotes/quote_confirm_delete.html'
    success_url = reverse_lazy('quotes:quote_list')

def generate_pdf(request, quote_id):
    BASE_DIR = settings.BASE_DIR
    # Create buffer and canvas
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    
    # Get quote data
    quote = Quote.objects.get(id=quote_id)
    
    # Set font
    p.setFont("Helvetica", 10)
    
    # Draw logo
    logo_path = os.path.join(BASE_DIR, 'quotes', 'static', 'quotes', 'logo.png')
    p.drawImage(logo_path, 250, 700, width=100, height=100)
    
    # Draw company name
    p.setFont("Helvetica", 14)
    p.drawString(250, 680, "EWA JOYERÍA")
    
    # Customer details section (left side)
    p.setFont("Helvetica", 10)
    p.drawString(50, 600, "EMITIDO A:")
    p.drawString(50, 580, f"{quote.client.name}")
    p.drawString(50, 560, f"{quote.client.email}")
    p.drawString(50, 540, f"{quote.client.phone}")
    
    # Quote details (right side)
    p.drawString(450, 600, "COTIZACIÓN")
    p.drawString(450, 580, f"FECHA: {quote.quote_date.strftime('%d.%m.%Y')}")
    p.drawString(450, 560, f"ID: {quote.quote_number}")
    
    # Table headers
    y_position = 480
    p.setFillColorRGB(0.9, 0.9, 0.9)  # Light gray background
    p.rect(50, y_position, 500, 20, fill=True)
    p.setFillColorRGB(0, 0, 0)  # Back to black text
    p.drawString(60, y_position + 5, "DESCRIPCIÓN")
    p.drawString(300, y_position + 5, "VALOR")
    p.drawString(400, y_position + 5, "QTY")
    p.drawString(480, y_position + 5, "TOTAL")
    
    # Quote content
    y_position -= 30
    # Split description into lines that fit within 220 points width
    description_lines = simpleSplit(quote.quote_description, p._fontname, p._fontsize, 220)
    
    # Draw each line of the description
    for line in description_lines:
        p.drawString(60, y_position, line)
        y_position -= 15  # Move down 15 points for next line
    
    # Reset y_position to the highest line for other columns
    y_position += (len(description_lines) - 1) * 15  # Move back up
    
    # Draw other columns
    p.drawString(300, y_position, f"COP {quote.quote_total:,.0f}")
    p.drawString(400, y_position, "1")
    p.drawString(480, y_position, f"COP {quote.quote_total:,.0f}")
    
    # Adjust y_position for next section
    y_position -= max(30, len(description_lines) * 15)  # Use the larger of standard spacing or text height
    
    # ... rest of the code ...
    p.setFillColorRGB(0.9, 0.9, 0.9)
    p.rect(50, y_position, 500, 20, fill=True)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(400, y_position + 5, "TOTAL")
    p.drawString(480, y_position + 5, f"COP {quote.quote_total:,.0f}")
    
    # Notes section
    y_position -= 40
    p.drawString(50, y_position, "Notas:")
    p.drawString(50, y_position - 20, quote.quote_additional_notes)
    
    # Footer
    y_position = 150  # Adjust this value as needed
    
    # DETALLES section (left side)
    p.drawString(50, y_position, "DETALLES")
    p.drawString(50, y_position - 20, "EWA joyería solicita el 60% de la")
    p.drawString(50, y_position - 35, "cotización para iniciar.")
    p.drawString(50, y_position - 50, "Métodos de pago:")
    p.drawString(50, y_position - 65, "Daviplata-Nequi: 3105458202")
    p.drawString(50, y_position - 80, "Cuenta de Ahorros Davivienda:")
    p.drawString(50, y_position - 95, "457900065071")
    p.drawString(50, y_position - 110, "Para más información puede")
    p.drawString(50, y_position - 125, "contactarnos aquí")
    
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
    response["Content-Disposition"] = "inline; filename={}".format(f"cotizacion_{quote.id}.pdf")
    return response

def create_invoice(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    
    request.session['invoice_initial_data'] = {
        'client': quote.client.id,  # Store ID instead of object
        'invoice_number': quote.quote_number,
        'invoice_total': str(quote.quote_total),  # Convert Decimal to string
        'additional_notes': quote.quote_additional_notes,
    }

    if quote.quote_product_type == 'Anillo de Compromiso' or quote.quote_product_type == 'Anillo de Matrimonio':
        return redirect('invoices:invoices_create_for_item')
    elif quote.quote_product_type == 'A medida' or quote.quote_product_type == 'Otro':
        request.session['invoice_initial_data']['description'] = quote.quote_description
        return redirect('invoices:invoices_create_for_customized')
    else:
        return redirect('invoices:invoices_create_for_customized')
    

