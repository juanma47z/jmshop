from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    date_register = models.DateTimeField(auto_now_add=True, verbose_name='fecha de registro')

    class Main:
        pass
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, verbose_name='categoria')
    name_product = models.CharField(max_length=200, verbose_name='nombre producto')
    description = models.TextField(null=True, verbose_name='descripcion')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='precio')
    date_register = models.DateTimeField(auto_now_add=True, verbose_name='fecha de registro')
    imagen = models.ImageField(upload_to='product', blank=True)

    def __str__(self):
        return self.name_product
