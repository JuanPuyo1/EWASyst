from django.shortcuts import render
from .models import Quote
from .forms import QuoteForm
from django.urls import reverse_lazy, reverse
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from invoices.models import Invoice
from invoices.forms import InvoiceForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#Generar PDF
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import os
from django.conf import settings
from reportlab.lib.utils import simpleSplit
# Create your views here.

class QuoteView(LoginRequiredMixin, ListView):
    model = Quote
    template_name = 'quotes/quotes_list.html'
    context_object_name = 'quotes'
    

class QuoteCreateView(LoginRequiredMixin, CreateView):
    model = Quote
    form_class = QuoteForm
    template_name = 'quotes/quotes_create.html'
    success_url = reverse_lazy('quotes:quotes_list')
    
class QuoteDetailView(LoginRequiredMixin, DetailView):
    model = Quote
    template_name = 'quotes/quotes_detail.html'
    context_object_name = 'quote'

class QuoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Quote
    form_class = QuoteForm
    template_name = 'quotes/quotes_create.html'

    success_url = reverse_lazy('quotes:quotes_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quote'] = Quote.objects.get(id=self.kwargs['pk'])
        return context

class QuoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Quote
    template_name = 'quotes/quotes_confirm_delete.html'
    success_url = reverse_lazy('quotes:quotes_list')

@login_required
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
    logo_path = os.path.join(BASE_DIR, 'quotes', 'static', 'quotes', 'img', 'logo.png') 
    p.drawImage(logo_path, 250, 700, width=100, height=100)
    
    # Draw company name
    p.setFont("Helvetica", 14)
    p.drawString(250, 680, "EWA JOYERÍA")
    
    # Customer details section (left side)
    p.setFont("Helvetica", 10)
    p.drawString(50, 600, "EMITIDO A:")
    p.drawString(50, 580, f"{quote.client.name}")
    if quote.client.document_number:
        p.drawString(50, 560, f"{quote.client.document_type} {quote.client.document_number}")
    else:
        p.drawString(50, 560, f"")
    if quote.client.email:
        p.drawString(50, 540, f"{quote.client.email}")
    else:
        p.drawString(50, 540, f"")
    if quote.client.phone:
        p.drawString(50, 520, f"{quote.client.phone}")
    else:
        p.drawString(50, 520, f"")
    
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

    # Save the y_position after the last description line
    after_description_y = y_position

    # Draw other columns for the main row (align with the first line of description)
    main_row_y = after_description_y + 15 * len(description_lines)
    p.drawString(300, main_row_y, f"COP {quote.quote_value:,.0f}")
    p.drawString(400, main_row_y, f"{quote.quote_quantity}")
    p.drawString(480, main_row_y, f"COP {quote.quote_value:,.0f}")

    

    # Discount row (if any)
    if quote.quote_discount is not None and quote.quote_discount > 0:
        # Split by newlines first, then wrap each line
        discount_desc_lines = []
        for desc_line in (quote.quote_discount_description or "Descuento").split('\n'):
            discount_desc_lines.extend(simpleSplit(desc_line, p._fontname, p._fontsize, 220))
        discount_y = after_description_y - 15  # Start right after the description

        for i, line in enumerate(discount_desc_lines):
            p.drawString(60, discount_y, line)
            # Only the first line gets the value/qty/total columns
            if i == 0:
                p.drawString(300, discount_y, f"COP {- quote.quote_discount:,.0f}")
                p.drawString(400, discount_y, "")  # QTY empty
                p.drawString(480, discount_y, f"COP {- quote.quote_discount:,.0f}")  # TOTAL empty
            discount_y -= 15

        y_position = discount_y  # Update y_position for the next section
    else:
        y_position = after_description_y

    # Now y_position is correct for the next section (e.g., TOTAL row)
    y_position -= 15
    
    p.setFillColorRGB(0.9, 0.9, 0.9)
    p.rect(50, y_position, 500, 20, fill=True)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(400, y_position + 5, "TOTAL")
    p.drawString(480, y_position + 5, f"COP {quote.quote_total:,.0f}")
    
    # Notes section
    y_position -= 40
    p.drawString(50, y_position, "Notas:")
    y_position -= 20  # Move down for the first note line

    if quote.quote_additional_notes:
        for line in quote.quote_additional_notes.split('\n'):
            # Split the line to fit within 500 points width
            wrapped_lines = simpleSplit(line, p._fontname, p._fontsize, 500)
            for wrapped_line in wrapped_lines:
                p.drawString(50, y_position, wrapped_line)
                y_position -= 15  # Move down for each wrapped line
    else:
        p.drawString(50, y_position, "No hay notas adicionales")
    
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
    p.drawString(50, y_position - 125, "contactarnos www.ewajoyeria.com")
    
    # GRACIAS and signature (right side)
    p.drawString(450, y_position, "GRACIAS")
    
    # Draw signature
    sign_path = os.path.join(BASE_DIR, 'quotes', 'static', 'quotes', 'img', 'sign.jpg')
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
        'observation': quote.quote_description,
        'invoice_quantity': quote.quote_quantity,
        'additional_notes': quote.quote_additional_notes,
        'invoice_type': quote.quote_product_type,
    }

    return redirect('invoices:invoices_create')


class QuoteConfirmEmailView(LoginRequiredMixin, View):
    template_name = 'quotes/quotes_confirm_email.html'
    success_url = reverse_lazy('quotes:quotes_list')
    def get(self, request, *args, **kwargs):
        quote = Quote.objects.get(id=kwargs['quote_id'])
        return render(request, self.template_name, {'quote': quote})
    
    def post(self, request, *args, **kwargs):
        try:
            quote = Quote.objects.get(id=kwargs['quote_id'])
            send_email_quote(request, quote.id)
            messages.add_message(request, messages.SUCCESS, 'Cotización enviada correctamente')
            return redirect(self.success_url)
        except Exception as e:
            messages.add_message(request, messages.ERROR, f"Error: {e}")
            return HttpResponse(f"Error: {e}")

def send_email_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    subject = f"Cotización {quote.quote_number} EWA JOYERÍA"
    message_body = f"Buenas tardes, segun lo solicitado, la cotización {quote.quote_number} ha sido generada"
    from_email = settings.EMAIL_HOST_USER
    
    if subject and message_body and from_email and quote.client.email:
        try:
            # Create EmailMessage object
            email = EmailMessage(
                subject=subject,
                body=message_body,
                from_email=from_email,
                to=[quote.client.email]
            )
            
            # Generate PDF and attach it
            pdf_response = generate_pdf(request, quote_id)
            pdf_content = b''.join(pdf_response.streaming_content)
            
            email.attach(
                filename=f"cotizacion_{quote.quote_number}.pdf",
                content=pdf_content,
                mimetype='application/pdf'
            )
            
            # Send the email
            email.send()
            quote.email_sent = True
            quote.save()
            print("Email sent successfully")
            return HttpResponseRedirect(reverse('quotes:quotes_list'))
        except BadHeaderError:
            print("Invalid header found.")
            return HttpResponse("Invalid header found.")
        except Exception as e:
            print(f"Error sending email: {e}")
            return HttpResponse(f"Error sending email: {e}")
    else:
        return HttpResponse("Make sure all fields are entered and valid.")

