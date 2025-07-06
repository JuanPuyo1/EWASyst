from django.urls import path
from .views import QuoteView, QuoteCreateView, QuoteUpdateView, QuoteDeleteView, QuoteDetailView, generate_pdf, create_invoice

app_name = 'quotes'

urlpatterns = [
    path('', QuoteView.as_view(), name='quotes_list'),
    path('create/', QuoteCreateView.as_view(), name='quotes_create'),
    path('detail/<int:pk>/', QuoteDetailView.as_view(), name='quotes_detail'),
    path('update/<int:pk>/', QuoteUpdateView.as_view(), name='quotes_update'),
    path('delete/<int:pk>/', QuoteDeleteView.as_view(), name='quotes_delete'),
    path('generate_pdf/<int:quote_id>/', generate_pdf, name='generate_pdf'),
    path('create_invoice/<int:quote_id>/', create_invoice, name='create_invoice'),
]

