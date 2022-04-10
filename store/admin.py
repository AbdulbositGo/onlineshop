from django.contrib import admin

from .models import *

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = ["image"]
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "rating", "category", "active",]
    list_display_link = ["name"]
    list_editable = ["rating", "price", "active"]
    search_sields = ["name", "description"]
    prepopulated_fields = {"slug": ("name",)}

    inlines = [
        ProductImageAdmin
    ]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)  