from django.contrib import admin
from employee.models import *
import tablib
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources

@admin.register(Profile)
class ViewAdmin(ImportExportModelAdmin):
    pass
