from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Client
from .forms import ClientForm
from django.shortcuts import redirect

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


