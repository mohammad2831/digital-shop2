from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import Cart
from products.models import Products
from .forms import CartAddForm, CouponApplyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem, Coupon,CouponUsage
import datetime
from django.contrib import messages
import requests
import json
from django.conf import settings
from django.http import JsonResponse, HttpResponse



class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'orders/cart.html', {'cart':cart})


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Products, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if quantity <= product.stock:  
                cart.add(product, quantity)
                return redirect('orders:cart')
            else:
               
                messages.error(request, f'The requested quantity exceeds the available stock. Current stock: {product.stock}')
        return render(request, 'products/detail.html', {'product': product, 'form':form})        







class CartRemoveView(View):
	def get(self, request, product_id):
		cart = Cart(request)
		product = get_object_or_404(Products, id=product_id)
		cart.remove(product)
		return redirect('orders:cart')

		

class OrdersDetailView(LoginRequiredMixin,View):
	form_class = CouponApplyForm
	def get(self, request, order_id):
		order = get_object_or_404(Order, id=order_id)
		return render(request, 'orders/order.html', {'order':order, 'form':self.form_class})
	

class OrdersCreateView(LoginRequiredMixin,View):
	def get(self, request):
		cart = Cart(request)
		order = Order.objects.create(user=request.user)
		for item in cart:
			OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
		cart.clear()
		return redirect('orders:order_detail', order.id)		




class CouponApplyView(LoginRequiredMixin, View):
    form_class = CouponApplyForm

    def post(self, request, order_id):
        now = datetime.datetime.now()
        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code__exact=code, valid_from__lte=now, valid_to__gte=now, active=True)
            except Coupon.DoesNotExist:
                messages.error(request, 'This coupon does not exist', 'danger')
                return redirect('orders:order_detail', order_id)
            
            
            if CouponUsage.objects.filter(user=request.user, coupon=coupon).exists():
                messages.error(request, 'You have already used this coupon', 'danger')
                return redirect('orders:order_detail', order_id)
            
            order = Order.objects.get(id=order_id)
            order.discount = coupon.discount
            order.save()
            
            
            CouponUsage.objects.create(user=request.user, coupon=coupon)
            messages.success(request, 'Coupon applied successfully', 'success')
        else:
            messages.error(request, 'Invalid form submission', 'danger')
        
        return redirect('orders:order_detail', order_id)
	


class PaymentView(View):
    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        amount = order.get_total_price()  
        return render(request, 'orders/load.html', {'order':order, 'amount':amount})


class DetaiPay(View):
     def post(request):
          return render(request, 'orders/pay.html')
          


'''
class ZibalPaymentView(View):


    def post(self, request, order_id):
        # اطلاعات احراز هویت
        merchant_id = "zibal"  # مقدار واقعی را اینجا وارد کنید
        
        order = get_object_or_404(Order, id=order_id)

        amount = order.get_total_price()  # Assuming you have a method to get total price

        # اطلاعات سفارش
      
        
        # ساخت داده‌ها برای درخواست
        data = {
            "merchantId": merchant_id,
          
            "orderId": str(order.id),
            "amount": amount,
            "callbackUrl" : 'http://127.0.0.1:8080/orders/verify/',  
            "description": "Order payment",
           
        }
            

        # ارسال درخواست به زیبال
        url = "https://sandbox-api.zibal.ir/merchant/addOrder"
        response = requests.post(url, json=data)
        result = response.json()

        if result['result'] == 1:
            # هدایت به صفحه پرداخت
            zibal_id = result['zibalId']
            payment_url = f"https://gateway.zibal.ir/start/{zibal_id}"
            return HttpResponse(f"<a href='{payment_url}'>پرداخت</a>")
        else:
            return JsonResponse({"error": result['message']})
    

    
'''