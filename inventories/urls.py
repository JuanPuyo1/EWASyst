from django.urls import path
from . import views

urlpatterns = [
    path('inventories_list/', views.InventoriesListView.as_view(), name='inventories_list'),
]
