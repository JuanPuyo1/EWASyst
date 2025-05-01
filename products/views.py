from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Ring, Stone, ChainOrBracelet
from .forms import RingForm, StoneForm, ChainOrBraceletForm

# Create your views here.

class ProductsListView(View):
    def get(self, request):
        rings = Ring.objects.all()
        stones = Stone.objects.all()
        chain_or_bracelets = ChainOrBracelet.objects.all()
        return render(request, 'products/products_list.html', {
            'rings': rings,
            'stones': stones,
            'chain_or_bracelets': chain_or_bracelets
        })

class ProductsCreateListView(View):
    def get(self, request):
        return render(request, 'products/products_create_option.html')

class RingCreateView(CreateView):
    model = Ring
    form_class = RingForm
    template_name = 'products/products_create_ring.html'
    success_url = reverse_lazy('products:products_list')

class RingUpdateView(UpdateView):
    model = Ring
    form_class = RingForm
    template_name = 'products/products_create_ring.html'
    success_url = reverse_lazy('products:products_list')

class StoneCreateView(CreateView):
    model = Stone
    form_class = StoneForm
    template_name = 'products/products_create_stone.html'
    success_url = reverse_lazy('products:products_list')

class StoneUpdateView(UpdateView):
    model = Stone
    form_class = StoneForm
    template_name = 'products/products_create_stone.html'
    success_url = reverse_lazy('products:products_list')

class ChainOrBraceletCreateView(CreateView):
    model = ChainOrBracelet
    form_class = ChainOrBraceletForm
    template_name = 'products/products_create_chain_or_bracelet.html'
    success_url = reverse_lazy('products:products_list')    

class ChainOrBraceletUpdateView(UpdateView):
    model = ChainOrBracelet
    form_class = ChainOrBraceletForm
    template_name = 'products/products_create_chain_or_bracelet.html'
    success_url = reverse_lazy('products:products_list')

def products_delete(request, id):
    ring = Ring.objects.get(id=id)
    ring.delete()
    return redirect('products:products_list')