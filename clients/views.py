from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Q

from .models import Client
from .forms import ClientForm
from django.contrib.auth.mixins import LoginRequiredMixin
from dal import autocomplete
# Create your views here.


class ClientsListView( LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/clients_list.html'
    context_object_name = 'clients'

class ClientsCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ClientForm()
        return render(request, 'clients/clients_create.html', {'form': form })

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.GET.get('next'))
            return redirect(request.GET.get('next') or reverse_lazy('clients:clients_list'))
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
    
class ClientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Client.objects.all()
        if not self.request.user.is_authenticated:
            return Client.objects.none()
        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

    
