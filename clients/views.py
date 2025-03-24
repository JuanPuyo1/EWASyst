from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Client
from .forms import ClientForm
# Create your views here.


class ClientsListView(ListView):
    model = Client
    template_name = 'clients/clients_list.html'
    context_object_name = 'clients'

class ClientsCreateView(View):
    def get(self, request):
        form = ClientForm()
        return render(request, 'clients/clients_create.html', {'form': form})

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients:clients_list')
        return render(request, 'clients/clients_create.html', {'form': form})


class ClientsUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/clients_update.html'
    success_url = reverse_lazy('clients:clients_list')

def clients_delete(request, pk):
    client = Client.objects.get(id=pk)
    client.delete()
    return redirect('clients:clients_list')
    

