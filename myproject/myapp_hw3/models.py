from django.db import models
from django.core.validators import MinValueValidator



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    date_registered = models.DateField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    quantity_products = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', default='products/default.jpg')

    def __str__(self):
        return f'Name_product: {self.name}, Price: {self.price}, Balance(Kol-vo):{self.quantity_products}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)