# Generated by Django 4.2.8 on 2023-12-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_order_rename_image_source_products_img_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='title',
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Электронная почта'),
        ),
    ]
