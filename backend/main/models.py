from django.db import models

class Order(models.Model):
    name = models.CharField("Имя", max_length=50)
    phone = models.CharField("Номер телефона", max_length=12)
    email = models.EmailField("Электронная почта", max_length=50)
    adress = models.CharField("Адрес", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
class Products(models.Model):
    img = models.ImageField("Карта товара", upload_to='images/', blank=False)



