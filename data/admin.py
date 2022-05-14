from django.contrib import admin
from .models import Product, Recommendations, Category, Ordering, Color, TheSize


class TheSizeInlines(admin.TabularInline):
    model = TheSize
    extra = 0


class ColorInlines(admin.TabularInline):
    model = Color
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ColorInlines, TheSizeInlines]
    list_display = ['name', 'price', 'are_available']
    list_filter = ['name', 'price', 'are_available']
    search_fields = ['name', 'price', 'are_available']
    fieldsets = (
        ('Описание продукта', {
            'fields': ('name', 'description')
        }),
        ('Характеристика продукта', {
            'fields': ('img', 'price', 'are_available', 'amount', 'sale', 'category')
        }),
    )


class OrderingAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'region']
    list_filter = ['full_name', 'phone_number', 'region']
    search_fields = ['full_name', 'phone_number', 'region']


admin.site.register(Product, ProductAdmin)
admin.site.register(Recommendations)
admin.site.register(Category)
admin.site.register(Ordering, OrderingAdmin)
