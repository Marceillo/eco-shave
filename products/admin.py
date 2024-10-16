from django.contrib import admin
from .models import Product, Category, PreviewImage
from star_ratings.models import Rating

# Register your models here.
class PreviewImageInline(admin.TabularInline):
    model = PreviewImage
    extra = 1 


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        # 'rating',
        'image',
    )

    ordering = ('sku',)
    inlines = [PreviewImageInline]
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)