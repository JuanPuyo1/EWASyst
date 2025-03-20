from django.urls import path
from . import views

urlpatterns = [
    path('invoices_list/', views.InvoicesListView.as_view(), name='invoices_list'),
]
