from django.contrib import admin
from inflows.models import Inflow

# Register your models here.
@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'created_at', 'updated_at',)
    search_fields = ('supplier__name', 'product__title',)