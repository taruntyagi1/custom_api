from django.contrib import admin
from category.models import Category

# Register your models here.
class customcategory(admin.ModelAdmin):
    list_display = ['category_name','slug','is_active']
    prepopulated_fields = {'slug': ('category_name',)}
admin.site.register(Category,customcategory)
