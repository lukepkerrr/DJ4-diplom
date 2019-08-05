from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Изображение')
    published_at = models.DateField(verbose_name='Дата публикации')
    users = models.ManyToManyField(User, through='Item_in_cart', verbose_name='Заказавшие', related_name='items')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Type(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.title


class Section(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    articles = models.ManyToManyField(Item, verbose_name='Товары', related_name='sections')
    type = models.ForeignKey(Type, verbose_name='Тип', related_name='sections', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title


class Item_in_cart(models.Model):

    item = models.ForeignKey(Item, verbose_name='Товар', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return '{} {} {}'.format(self.item, self.user, self.amount)


class Jumbotron(models.Model):

    first_field = models.TextField(verbose_name='Первая строка')
    second_field = models.TextField(verbose_name='Вторая строка')
    section = models.OneToOneField(Section, verbose_name='Раздел', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Строка на главной'
        verbose_name_plural = 'Строки на главной'

    def __str__(self):
        return '{} {} {}'.format(self.first_field, self.second_field, self.section)

class Comment(models.Model):

    name = models.CharField(max_length=256, verbose_name='Имя')
    text = models.TextField(verbose_name='Описание')
    score = models.IntegerField(verbose_name='Оценка')
    item = models.ForeignKey(Item, verbose_name='Товар', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return '{} {} {}'.format(self.name, self.score, self.item)