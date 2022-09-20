from django.db import models


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=30)
    ingredients = models.ManyToManyField('Ingredients')
    price = models.DecimalField (max_digits=5, decimal_places=2)
    weight = models.PositiveIntegerField()
    image = models.ImageField(upload_to='menu/static', blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Пицца'
        verbose_name = 'Пицца'


class Ingredients(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = 'Ингридиенты'
        verbose_name = 'Ингридиенты'

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField (max_digits=4, decimal_places=2)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu/static', blank=True)

    class Meta:
        verbose_name_plural = 'Напитки'
        verbose_name = 'Напитки'


class Product(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name
