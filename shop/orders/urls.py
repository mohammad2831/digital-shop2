from django.urls import path
from . import views

app_name= 'orders'
urlpatterns =[
    path('create/', views.OrdersCreateView.as_view(), name = 'order_create'),
    path('detail/<int:order_id>',views.OrdersDetailView.as_view(), name = 'order_detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>', views.CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>', views.CartRemoveView.as_view(), name ='cart_remove'),
    path('apply/<int:order_id>', views.CouponApplyView.as_view(), name='coupon_apply'),
    path('pay/<int:order_id>', views.PaymentView.as_view(), name='order_pay'),


    path('payment/', views.DetaiPay.as_view(), name='detail_pay')

    
    
]