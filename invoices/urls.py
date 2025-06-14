from django.urls import path
from . import views

app_name = 'invoices'

urlpatterns = [
    path('invoices_list/', views.InvoicesListView.as_view(), name='invoices_list'),
    path('invoices_create/', views.InvoicesCreate.as_view(), name='invoices_create'),
    path('invoices_delete/<int:pk>/', views.InvoicesConfirmDeleteView.as_view(), name='invoices_delete'),
    path('generate_pdf_item/<int:invoice_id>/', views.generate_pdf_item, name='generate_pdf_item'),
    path('invoices_confirm_delete/<int:pk>/', views.InvoicesConfirmDeleteView.as_view(), name='invoices_confirm_delete'),
]

