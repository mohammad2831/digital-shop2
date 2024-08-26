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
    

    


admin.site.register(Coupon)
admin.site.register(OrderItem)

