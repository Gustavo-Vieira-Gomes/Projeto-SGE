from django.contrib import admin
from brands.models import Brand
# Register your models here.

@admin.register(Brand)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at', )
    search_fields = ('name', )