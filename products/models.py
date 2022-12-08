from django.db import models
from category.models  import Category
from variants.models import Variants

# Create your models here.



class Products(models.Model):
    product_name = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length=100,unique=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='photo/products')
    variants = models.ForeignKey(Variants,on_delete=models.CASCADE,null = True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.product_name

