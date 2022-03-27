from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "rating", "category", "active",]
    list_display_link = ["name"]
    list_editable = ["rating", "price", "active"]
    search_sields = ["name", "description"]
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)