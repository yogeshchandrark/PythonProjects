from rolepermissions.roles import AbstractUserRole

class Manager(AbstractUserRole):
    available_permissions = {
        'create_employee_record': True,
        'edit_employee_record': True,
        'view_employee_record': True,
    }

class Employee(AbstractUserRole):
    available_permissions = {
        'view_employee_record': True,
    }
