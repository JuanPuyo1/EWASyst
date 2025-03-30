from django.urls import path
from . import views

app_name = 'inventories'

urlpatterns = [
    path('inventories_list/', views.InventoriesListView.as_view(), name='inventories_list'),
    path('inventories_create/', views.InventoriesCreateView.as_view(), name='inventories_create'),
    path('inventories_update/<int:pk>/', views.InventoriesUpdateView.as_view(), name='inventories_update'),
    path('inventories_delete/<int:pk>/', views.InventoriesDeleteView.as_view(), name='inventories_delete'),
]
