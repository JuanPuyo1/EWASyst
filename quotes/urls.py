from django.urls import path
from .views import QuoteView, QuoteCreateView, QuoteUpdateView, QuoteDeleteView, generate_pdf, create_invoice

app_name = 'quotes'

urlpatterns = [
    path('', QuoteView.as_view(), name='quote_list'),
    path('create/', QuoteCreateView.as_view(), name='quote_create'),
    path('update/<int:pk>/', QuoteUpdateView.as_view(), name='quote_update'),
    path('delete/<int:pk>/', QuoteDeleteView.as_view(), name='quote_delete'),
    path('generate_pdf/<int:quote_id>/', generate_pdf, name='generate_pdf'),
    path('create_invoice/<int:quote_id>/', create_invoice, name='create_invoice'),
]

