from django.db import models
from django.core.validators import MinValueValidator



class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя клиента')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    address = models.CharField(max_length=150, verbose_name='Адрес')
    date_registered = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], verbose_name='Цена')
    quantity_products = models.PositiveSmallIntegerField(default=0, verbose_name='Кол-во')
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(upload_to='products/', default='products/default.jpg', verbose_name='Изображение')

    # def __str__(self):
    #     return f'Name_product: {self.name}, Price: {self.price}, Balance(Kol-vo):{self.quantity_products}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Номер Заказа')
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Сумма заказа')
    date_ordered = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"