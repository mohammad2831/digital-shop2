from django.contrib import admin
from .models import Category_Type, Category_Company, Products,Attribute,ProductAttribute, ProductView
from .forms import ProductsForm, ProductAttributeForm

class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class CategoryCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('type',)

class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    form = ProductAttributeForm
    extra = 1

class ProductsAdmin(admin.ModelAdmin):
    form = ProductsForm
    list_display = ('name', 'category', 'stock', 'price', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated', 'category')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductAttributeInline]


class ProductViewAdmin(admin.ModelAdmin):

    list_display = ('product', 'ip_address', 'timestamp')
    list_filter = ('timestamp',)



admin.site.register(Category_Type, CategoryTypeAdmin)
admin.site.register(Category_Company, CategoryCompanyAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Attribute)
admin.site.register(ProductAttribute)
admin.site.register(ProductView, ProductViewAdmin)