from django.shortcuts import render
from Inventory.models import inventory
# Create your views here.
def inventory_test(request):
    inventory_data = inventory.objects.order_by('siteID')
    data_acc = {'inventory': inventory_data}
    return render(request, 'Inventory/inventory.html', context=data_acc)
