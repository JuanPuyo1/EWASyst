from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Client
from .forms import ClientForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ClientsListView( LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/clients_list.html'
    context_object_name = 'clients'

class ClientsCreateView(LoginRequiredMixin, View):
    def get(self, request, flag):

        form = ClientForm()
        return render(request, 'clients/clients_create.html', {'form': form})

    def post(self, request, flag):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients:clients_list')
        return render(request, 'clients/clients_create.html', {'form': form})


class ClientsUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/clients_update.html'
    success_url = reverse_lazy('clients:clients_list')

class ClientsDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'clients/client_delete.html'
    success_url = reverse_lazy('clients:clients_list')
    

