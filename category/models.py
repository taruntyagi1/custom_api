from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200, unique = True)
    slug = models.SlugField(max_length=200, unique = True)
    description = models.TextField()
    image = models.ImageField(upload_to='photo/category')
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Category'


    def __str__(self):
        return self.category_name