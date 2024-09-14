from django.contrib import admin
from . models import Order
from . models import OrderItem, Coupon
from django import forms



class OrserItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    paid = forms.BooleanField()
    list_display = ('id', 'user', 'updated','paid', )
    list_filter = ('paid',)
    inlines = (OrserItemInline,)
    
<<<<<<< HEAD
    def save_model(self, request, obj, form, change):
        if change and 'paid' in form.changed_data and obj.paid:
           
            self.reduce_product_stock(obj)
        super().save_model(request, obj, form, change)

    def reduce_product_stock(self, order):
        
        order_items = OrderItem.objects.filter(order=order)
        for item in order_items:
            product = item.product  
            product.stock -= item.quantity  
            product.save()
=======

>>>>>>> c42e347d (atomic transaction)
    


admin.site.register(Coupon)
<<<<<<< HEAD
=======
admin.site.register(OrderItem)
>>>>>>> c42e347d (atomic transaction)

