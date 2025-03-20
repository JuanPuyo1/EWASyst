from django.shortcuts import render
from django.views import View
# Create your views here.
class InventoriesListView(View):
    def get(self, request):
        return render(request, 'inventories/inventories_list.html')

