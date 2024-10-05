from django.contrib import admin
from outflows.models import Outflow
# Register your models here.


@admin.register(Outflow)
class OutflowAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at', 'updated_at',)
    search_fields = ('product__title', )