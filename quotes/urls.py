from django.urls import path
from .views import QuoteView, QuoteCreateView, QuoteUpdateView, QuoteDeleteView, QuoteDetailView, generate_pdf, create_invoice, send_email_quote, QuoteConfirmEmailView

app_name = 'quotes'

urlpatterns = [
    path('', QuoteView.as_view(), name='quotes_list'),
    path('create/', QuoteCreateView.as_view(), name='quotes_create'),
    path('detail/<int:pk>/', QuoteDetailView.as_view(), name='quotes_detail'),
    path('update/<int:pk>/', QuoteUpdateView.as_view(), name='quotes_update'),
    path('delete/<int:pk>/', QuoteDeleteView.as_view(), name='quotes_delete'),
    path('generate_pdf/<int:quote_id>/', generate_pdf, name='generate_pdf'),
    path('create_invoice/<int:quote_id>/', create_invoice, name='create_invoice'),
    path('confirm_email/<int:quote_id>/', QuoteConfirmEmailView.as_view(), name='confirm_email'),
    path('send_email_quote/<int:quote_id>/', send_email_quote, name='send_email_quote'),
]

