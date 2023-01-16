from django.db import models
from django.urls import reverse


class Phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    price = models.CharField(max_length=30, verbose_name='Цена')
    release_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода')
    lte_exists = models.CharField(max_length=200, default=True, verbose_name='LTE')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}, {self.image}, {self.price}, {self.slug}'

    def get_absolut_url(self):
        return reverse('name', kwargs={'slug': self.slug})