from django.urls import path
from .views import ProductsListView, ProductsCreateListView, RingCreateView, StoneCreateView, ChainOrBraceletCreateView, products_delete

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('create/', ProductsCreateListView.as_view(), name='products_create_option'),
    path('create/ring/', RingCreateView.as_view(), name='products_create_ring'),
    path('create/stone/', StoneCreateView.as_view(), name='products_create_stone'),
    path('create/chain-or-bracelet/', ChainOrBraceletCreateView.as_view(), name='products_create_chain_or_bracelet'),
    path('delete/<int:id>/', products_delete, name='products_delete'),
]