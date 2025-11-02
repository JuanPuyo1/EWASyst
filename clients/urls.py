from django.urls import path
from . import views
from .views import ClientsListView, ClientsCreateView, ClientsUpdateView, ClientsDeleteView, ClientAutocomplete

app_name = 'clients'

urlpatterns = [
    path('clients_list/', ClientsListView.as_view(), name='clients_list'),
    path('clients_create/', ClientsCreateView.as_view(), name='clients_create'),
    path('clients_update/<int:pk>/', ClientsUpdateView.as_view(), name='clients_update'),
    path('clients_delete/<int:pk>/', ClientsDeleteView.as_view(), name='clients_delete'),
    path('clients_autocomplete/', ClientAutocomplete.as_view(), name='clients_autocomplete'),
]