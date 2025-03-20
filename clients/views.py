from django.shortcuts import render
from django.views import View
# Create your views here.

class ClientsListView(View):
    def get(self, request):
        return render(request, 'clients/clients_list.html')
