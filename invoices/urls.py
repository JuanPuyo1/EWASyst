from django.urls import path
from . import views

app_name = 'invoices'

urlpatterns = [
    path('invoices_list/', views.InvoicesListView.as_view(), name='invoices_list'),
    path('invoices_create_option/', views.InvoicesCreateOptionView.as_view(), name='invoices_create_option'),
    path('invoices_create_for_item/', views.InvoicesCreateForItemView.as_view(), name='invoices_create_for_item'),
    path('invoices_create_for_customized/', views.InvoicesCreateForCustomizedView.as_view(), name='invoices_create_for_customized'),
    path('invoices_delete/<int:pk>/', views.invoices_delete, name='invoices_delete'),
    path('generate_pdf_item/<int:invoice_id>/', views.generate_pdf_item, name='generate_pdf_item'),
]

