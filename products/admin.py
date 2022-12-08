from django.contrib import admin
from products.models import Products,Variants

# Register your models here.
class customproduct(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ['product_name','slug','price','stock','is_available','is_active']
admin.site.register(Products,customproduct)
admin.site.register(Variants)