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
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


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
	










@method_decorator(csrf_exempt, name='dispatch')
class PaymentView(View):
    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        print(order_id)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")


     #   order_item_id = order.items.all()
        amount = order.get_total_price()

        
        data = {
            'pin': 'sandbox',
            'amount': amount,
            'callback': 'http://127.0.0.1:8000/orders/payment/callback/',
            'invoice_id': str(order.id),
        }
        
        response = requests.post('https://panel.aqayepardakht.ir/api/v2/create', data=data)
        json_data = json.loads(response.text)

        if response.status_code == 200 and json_data.get('status') == 'success':
            transid = json_data.get('transid')
            if transid:
                return redirect(f'https://panel.aqayepardakht.ir/startpay/sandbox/{transid}')
      
        return render(request, 'orders/load.html')





@method_decorator(csrf_exempt, name='dispatch')
class PaymentCallbackView(View):
    def post(self, request):
        status = request.POST.get('status')
        transid = request.POST.get('transid')
        invoice_id_str = request.POST.get('invoice_id')
        print(invoice_id_str)
       
        print(type(invoice_id_str))

        invoice_id_int = int(invoice_id_str)

        if status == "1":  
            try:
                order = get_object_or_404(Order, id=invoice_id_int)
                order_items = order.items.all() 
    
                products = [item.product for item in order_items]

                
                print(products)
                
                
                for item in order_items:
                    product = item.product
                    product.stock -= item.quantity
                    product.save() 
                
              
                return render(request, 'orders/load.html')


            except OrderItem.DoesNotExist:
                print("OrderItem with the given ID does not exist")
               
                return redirect('orders:order_create')

        else:
            print("----------------------------------------------------------")
       
            return redirect('orders:order_create')


