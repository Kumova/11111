from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=30)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    release_date = models.DateTimeField(auto_now_add=True)
    lte_exists = models.CharField(max_length=200, default=True)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return f'{self.name}, {self.price}: {self.image}'

