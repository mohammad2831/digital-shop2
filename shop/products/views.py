from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Products, Category_Type, ProductAttribute, ProductView
from orders.forms import CartAddForm
from ipware import get_client_ip


class AllView(View):
    def get(self, request):
        types = Category_Type.objects.all()
        categories_with_products = {}
        for category in types:
            categories_with_products[category] = Products.objects.filter(type=category)
        return render(request, 'products/main.html', {'categories_with_products': categories_with_products})
    




class DetailProductView(View):
    def get(self, request, slug):
        form = CartAddForm() 
        product = get_object_or_404(Products, slug=slug)
        attr =  product.product_attributes.all()


        ip_address, is_routable = get_client_ip(request)
        session_key = request.session.session_key
        user = request.user if request.user.is_authenticated else None

        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        # Check if the view already exists
        if not ProductView.objects.filter(product=product, ip_address=ip_address, session_key=session_key, user=user).exists():
            ProductView.objects.create(product=product, ip_address=ip_address, session_key=session_key, user=user)



        return render(request, 'products/detail.html', {'product': product, 'form':form, 'attr':attr})
        






