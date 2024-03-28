from django.contrib import admin

from product.models import Product, Category, Review, Tag

# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'size')
    search_fields = ('title', 'price')

    def save_model(self, request, obj, form, change):
        obj.title = obj.title.capitalize()
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'product_id')
    search_fields = ('name', 'product_id')

    def save_model(self, request, obj, form, change):
        obj.title = obj.title.capitalize()
        super().save_model(request, obj, form, change)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'text', 'id')
    search_fields = ('text', 'product_id')

    def save_model(self, request, obj, form, change):
        obj.title = obj.title.capitalize()
        super().save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','text')
    search_fields = ('text', 'id')

    def save_model(self, request, obj, form, change):
        obj.title = obj.title.capitalize()
        super().save_model(request, obj, form, change)