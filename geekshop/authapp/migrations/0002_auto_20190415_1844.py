# Generated by Django 2.1.7 on 2019-04-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
    ]
