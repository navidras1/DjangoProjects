from itertools import product

from django.db import models
from django.urls import reverse
from slugify import slugify


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='Ecom/images')
    slug = models.SlugField(unique=True, blank=True)
    stock = models.IntegerField()
    active = models.BooleanField()

    def save(self,*args,**kwargs):
        if not self.slug:
            self_slug = slugify(self.name)
            slug = self_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{self_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args,**kwargs)


    def getAbsoluteUrl(self):
        return  reverse('detail',args=[self.slug])

