# Generated by Django 2.1.7 on 2019-04-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_productcategory_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
    ]