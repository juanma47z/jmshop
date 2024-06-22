from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_register')
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'price')
    list_editable = ('price',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
