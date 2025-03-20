from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientsListView.as_view(), name='clients_list'),
]