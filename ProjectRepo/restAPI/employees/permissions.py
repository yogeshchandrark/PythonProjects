from rolepermissions.permissions import register_object_checker
from restAPI.roles import Manager, Employee

@register_object_checker()
def access_employees(role, user, employees):
    if role == Manager:
        return True

    if user.employees == employees:
        return True

    return False
