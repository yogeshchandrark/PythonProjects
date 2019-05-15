from django.shortcuts import render

# Create your views here.
def lab_test(labrequest):
    labdictlist = {'Lab_test': 'This is Inventory page !!'}
    return render(labrequest, 'LabRequest/labrequest.html', context=labdictlist)
