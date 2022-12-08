from django.db import models


# Create your models here.
class Variants(models.Model):
    title = models.CharField(max_length=100,unique=True)
    price = models.IntegerField()
    description = models.TextField()

    image = models.ImageField(upload_to='photo/variants')

    class Meta:
        verbose_name_plural = 'Variants'


    def __str__(self):
        return self.title