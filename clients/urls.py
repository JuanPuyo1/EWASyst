from django.urls import path
from . import views
from .views import ClientsListView, ClientsCreateView, ClientsUpdateView

app_name = 'clients'

urlpatterns = [
    path('clients_list/', ClientsListView.as_view(), name='clients_list'),
    path('clients_create/<flag>/', ClientsCreateView.as_view(), name='clients_create'),
    path('clients_update/<int:pk>/', ClientsUpdateView.as_view(), name='clients_update'),
    path('clients_delete/<int:pk>/', views.clients_delete, name='clients_delete'),
]