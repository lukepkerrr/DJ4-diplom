# Generated by Django 2.2.3 on 2019-07-30 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='item',
            name='published_at',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
    ]
