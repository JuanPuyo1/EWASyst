from django.urls import path
from . import views

app_name = 'invoices'

urlpatterns = [
    path('invoices_list/', views.InvoicesListView.as_view(), name='invoices_list'),
    path('invoices_create_list/', views.InvoicesCreateListView.as_view(), name='invoices_create_list'),
    path('invoices_create_for_item/', views.InvoicesCreateForItemView.as_view(), name='invoices_create_for_item'),
]

