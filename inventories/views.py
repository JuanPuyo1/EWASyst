from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, ListView
from .forms import InventoryForm
from .models import Inventory
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class InventoriesListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = 'inventories/inventories_list.html'
    context_object_name = 'inventories'

class InventoriesCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = InventoryForm()
        return render(request, 'inventories/inventories_create.html', {'form': form})
    
    def post(self, request):
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventories:inventories_list')
        return render(request, 'inventories/inventories_create.html', {'form': form})

class InventoriesUpdateView(LoginRequiredMixin, UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventories/inventories_update.html'
    success_url = reverse_lazy('inventories:inventories_list')

class InventoriesDeleteView(LoginRequiredMixin, DeleteView):
    model = Inventory
    template_name = 'inventories/inventories_delete.html'
    success_url = reverse_lazy('inventories:inventories_list')

