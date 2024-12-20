from django.contrib import admin
from .models import Product, Category, PreviewImage
from star_ratings.models import Rating


class PreviewImageInline(admin.TabularInline):
    model = PreviewImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'is_active',
        'get_main_image',
        'get_preview_images',
    )

    def get_main_image(self, obj):
        return obj.image.url if obj.image else 'No image'

    def get_preview_images(self, obj):
        return (
            ', '.join([img.image.url for img in obj.previewimage_set.all()])
            or 'No preview images'
        )

    ordering = ('sku',)
    inlines = [PreviewImageInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)
