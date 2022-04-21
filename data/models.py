from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, DecimalValidator



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
    img = models.ImageField('Картинка', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"

    name = models.CharField('Название', max_length=100, default='Продукт', validators=[
        RegexValidator(
            regex=r'\.$',
            message='уберите точку!',
            inverse_match=True,
        )
    ])
    img = models.ImageField('Картинка', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', null=True, validators=[
        DecimalValidator(
            max_digits=8,
            decimal_places=2,
        )
    ])
    description = models.TextField('Описание', blank=True, null=True)
    are_available = models.BooleanField('имеется в наличии', default=True)
    amount = models.IntegerField('Количество товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'{self.name}'


class Discount(models.Model):

    class Meta:
        verbose_name = 'Скидкa'
        verbose_name_plural = 'Скидки'

    discount = models.IntegerField('Скидка', blank=True, null=True, validators=[
        MinValueValidator(
            limit_value=1,
            message='Не менее 1!'
        )
    ])
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='discount_detail')

    def __str__(self):
        return f'{self.discount}'


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

    color = models.ImageField('расцветки', blank=True, null=True)
    color_name = models.CharField('Цвет', max_length=100)
    prod = models.ForeignKey(Product, on_delete=models.PROTECT,  verbose_name='расцветки', related_name='product_detail')

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
