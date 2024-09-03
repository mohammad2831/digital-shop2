from django.contrib import admin
from .models import Category_Type, Category_Company, Products,Attribute,ProductAttribute, ProductView, ProductLock
from django.shortcuts import redirect
from .forms import ProductsForm, ProductAttributeForm
from django.db import transaction
from django.utils import timezone



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




    

    def change_view(self, request, object_id, form_url='', extra_context=None):
        product = self.get_object(request, object_id)
        lock, created = ProductLock.objects.get_or_create(product=product)

        if lock.is_locked() and lock.locked_by != request.user:
            self.message_user(request, "This product is currently locked for editing by another admin.", level='warning')
            return redirect('admin:index')

        lock.lock_session = request.session.session_key
        lock.lock_timestamp = timezone.now()
        lock.locked_by = request.user
        lock.save()

        return super().change_view(request, object_id, form_url, extra_context)

    def response_change(self, request, obj):
        try:
            product_lock = ProductLock.objects.get(product=obj)
            product_lock.lock_session = None
            product_lock.lock_timestamp = None
            product_lock.locked_by = None
            product_lock.save()
        except ProductLock.DoesNotExist:
            pass
        return super().response_change(request, obj)




















class ProductViewAdmin(admin.ModelAdmin):
    list_display = ('product', 'ip_address', 'timestamp')
    list_filter = ('timestamp',)






admin.site.register(Category_Type, CategoryTypeAdmin)
admin.site.register(Category_Company, CategoryCompanyAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Attribute)
admin.site.register(ProductAttribute)
admin.site.register(ProductView, ProductViewAdmin)