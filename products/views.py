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

class RingCreateView(View):
    model = Ring
    form_class = RingForm
    template_name = 'products/products_create_ring.html'
    success_url = reverse_lazy('products:products_list')

    def get(self, request):
        form = self.form_class()
        return render(request, 'products/products_create_ring.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            ring_description = form.cleaned_data['ring_description']
            ring_size = form.cleaned_data['ring_size']
            ring_type = form.cleaned_data['ring_type']
            ring_quality = form.cleaned_data['ring_quality']
            ring_weight = form.cleaned_data['ring_weight']
            synthetic_stone = form.cleaned_data['synthetic_stone']
            jewellery_quantity = form.cleaned_data['jewellery_quantity']    
            certificate = form.cleaned_data['certificate']
            image = form.cleaned_data['image']
            ring = Ring.objects.create(jewellery_name=ring_description, ring_description=ring_description, ring_size=ring_size, ring_type=ring_type, ring_quality=ring_quality, ring_weight=ring_weight, synthetic_stone=synthetic_stone, jewellery_quantity=jewellery_quantity, certificate=certificate, image=image)
            ring.save()
            return redirect('products:products_list')
        print(form.errors)
        return render(request, 'products/products_create_ring.html', {

            'form': form
        })

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