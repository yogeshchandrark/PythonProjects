from django.shortcuts import render

# Create your views here.
def user_test(userrequest):
    userdictlist = {'Lab_test': 'This is Inventory page !!'}
    return render(userrequest, 'UserManagement/usermanagement.html', context=userdictlist)
