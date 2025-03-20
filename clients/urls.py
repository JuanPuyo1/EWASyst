from django.urls import path
from . import views
from .views import ClientsListView
urlpatterns = [
    path('clients_list/', ClientsListView.as_view(), name='clients_list'),
]