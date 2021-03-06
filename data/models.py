import os
from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator
from data.choice import CURRENCY_CHOICES, CURRENCY_DEFAULT
from main.utils import get_filename
from main.settings import AUTH_USER_MODEL
User = AUTH_USER_MODEL


def category_upload_to(instance, filename):
    new_img = get_filename(filename)
    return os.path.join('category', new_img)


def product_upload_to(instance, filename):
    new_img = get_filename(filename)
    return os.path.join('product', new_img)


def color_upload_to(instance, filename):
    new_img = get_filename(filename)
    return os.path.join('color', new_img)


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField('Категория', max_length=100, validators=[
        RegexValidator(
            regex=r'\.$',
            message='уберите точку!',
            inverse_match=True,
        )
    ])
    img = models.ImageField('Картинка', upload_to=category_upload_to, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"

    name = models.CharField('Название', max_length=100, validators=[
        RegexValidator(
            regex=r'\.$',
            message='уберите точку!',
            inverse_match=True,
        )
    ])
    img = models.ImageField('Картинка', upload_to=product_upload_to, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=8, choices=CURRENCY_CHOICES, default=CURRENCY_DEFAULT, verbose_name='Цена')
    description = models.TextField('Описание', blank=True, null=True)
    are_available = models.BooleanField('имеется в наличии', default=True)
    amount = models.IntegerField('Количество товара')
    sale = models.IntegerField('Скидка в процентах', blank=True, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='category_detail')
    favorites = models.BooleanField('', default=False)

    def get_sale(self):
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def __str__(self):
        return f'{self.name}'

    # def favorites_save(self):


class Review(models.Model):

    class Meta:
        verbose_name = 'Отзывы'
    creview = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    userview = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    review = models.TextField(help_text="Отзыв", verbose_name="Отзыв о продукте")
    created_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата отзыва')
    rating = models.PositiveSmallIntegerField(verbose_name=('рейтинг'), validators=[MaxValueValidator(5)])

    def __str__(self):
        return self.creview


class TheSize(models.Model):
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = "Размеры"

    title = models.CharField('Размер', max_length=6)
    prod = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Размер', related_name='prod_detail')

    def __str__(self):
        return f'{self.title}'


class Color(models.Model):
    class Meta:
        verbose_name = 'Расцветка'
        verbose_name_plural = 'Расцветки'

    color = models.ImageField('расцветки', upload_to=color_upload_to, blank=True, null=True)
    color_name = models.CharField('Цвет', max_length=100)
    prod = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='расцветки', related_name='product_detail')

    def __str__(self):
        return f'{self.color_name}'


class Recommendations(models.Model):
    name = models.CharField('Название', max_length=100)
    products = models.ManyToManyField(Product, verbose_name='Продукт', related_name='recommendations_detail')

    class Meta:
        verbose_name = 'рекомендация'
        verbose_name_plural = 'рекомендации'

    def __str__(self):
        return f'{self.name}'


DELIVERY = (('1', 'Доставка курьером'),
            ('2', 'самовывоз'),)

REGION = (
    ('1', 'Чуй'),
    ('2', 'Бишкек'),
    ('3', 'Ош'),
    ('4', 'Талас'),
    ('5', 'Иссык куль'),
    ('6', 'Джалал абад'),
    ('7', 'Баткен'),
)


class Ordering(models.Model):
    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адресы'

    full_name = models.CharField('Фио', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=20)
    region = models.CharField(choices=REGION, verbose_name='Область', max_length=100)
    price = models.DecimalField('Цена', max_digits=12, decimal_places=2)
    basket = models.TextField('Корзина')

    def __str__(self):
        return f'ID{self.full_name}'