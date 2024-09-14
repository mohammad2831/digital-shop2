from django.contrib import admin
<<<<<<< HEAD
from .models import Category_Type, Category_Company, Products,Attribute,ProductAttribute, ProductView
from .forms import ProductsForm, ProductAttributeForm
=======
from .models import Category_Type, Category_Company, Products,Attribute,ProductAttribute, ProductView, ProductLock
from django.shortcuts import redirect
from .forms import ProductsForm, ProductAttributeForm
from django.db import transaction,OperationalError
from django.utils import timezone
from django.http import HttpResponseForbidden
from django.contrib import messages


>>>>>>> c42e347d (atomic transaction)

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
<<<<<<< HEAD


class ProductViewAdmin(admin.ModelAdmin):

=======
    
    @transaction.atomic
    def change_view(self, request, object_id, form_url='', extra_context=None):
        try:
            with transaction.atomic():
                product = Products.objects.select_for_update().get(pk=object_id)
                
                
                response = super().change_view(request, object_id, form_url, extra_context)
                return response

        except OperationalError:
            messages.error(request, "try it latter.")
            return super().change_view(request, object_id, form_url, extra_context)

class ProductViewAdmin(admin.ModelAdmin):
>>>>>>> c42e347d (atomic transaction)
    list_display = ('product', 'ip_address', 'timestamp')
    list_filter = ('timestamp',)



<<<<<<< HEAD
=======



>>>>>>> c42e347d (atomic transaction)
admin.site.register(Category_Type, CategoryTypeAdmin)
admin.site.register(Category_Company, CategoryCompanyAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Attribute)
admin.site.register(ProductAttribute)
admin.site.register(ProductView, ProductViewAdmin)