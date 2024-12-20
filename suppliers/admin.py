from django.contrib import admin
from suppliers.models import Supplier
# Register your models here.


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', )
