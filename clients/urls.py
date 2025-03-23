from django.urls import path
from . import views
from .views import ClientsListView, ClientsCreateView

app_name = 'clients'

urlpatterns = [
    path('clients_list/', ClientsListView.as_view(), name='clients_list'),
    path('clients_create/', ClientsCreateView.as_view(), name='clients_create'),
]