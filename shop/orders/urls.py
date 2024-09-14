from django.urls import path
from . import views
<<<<<<< HEAD
=======
from home.views import HomeView 
>>>>>>> c42e347d (atomic transaction)

app_name= 'orders'
urlpatterns =[
    path('create/', views.OrdersCreateView.as_view(), name = 'order_create'),
    path('detail/<int:order_id>',views.OrdersDetailView.as_view(), name = 'order_detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>', views.CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>', views.CartRemoveView.as_view(), name ='cart_remove'),
    path('apply/<int:order_id>', views.CouponApplyView.as_view(), name='coupon_apply'),
<<<<<<< HEAD
    path('pay/<int:order_id>', views.PaymentView.as_view(), name='order_pay'),


    path('payment/', views.DetaiPay.as_view(), name='detail_pay')
=======


    path('pay/<int:order_id>', views.PaymentView.as_view(), name='order_pay'),


    path('payment/callback/', views.PaymentCallbackView.as_view(), name='payment_callback'),
    path('home/', HomeView.as_view(), name='home'),
    path('profile/<int:order_id>', views.ProfileOrderDetail.as_view(), name='profile_order_detail')

>>>>>>> c42e347d (atomic transaction)

    
    
]