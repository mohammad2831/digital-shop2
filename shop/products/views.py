from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Products, Category_Type, ProductAttribute, ProductView
from orders.forms import CartAddForm
from ipware import get_client_ip
<<<<<<< HEAD
=======
from home.forms import CommentForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
>>>>>>> c42e347d (atomic transaction)


class AllView(View):
    def get(self, request):
        types = Category_Type.objects.all()
        categories_with_products = {}
        for category in types:
            categories_with_products[category] = Products.objects.filter(type=category)
        return render(request, 'products/main.html', {'categories_with_products': categories_with_products})
    




class DetailProductView(View):
    def get(self, request, slug):
<<<<<<< HEAD
=======
        cache_key = f'product_detail_{slug}'
        product = cache.get(cache_key)
        if not product:
            product = get_object_or_404(Products, slug=slug)
            cache.set(cache_key, product, timeout=3600)

>>>>>>> c42e347d (atomic transaction)
        form = CartAddForm() 
        product = get_object_or_404(Products, slug=slug)
        attr =  product.product_attributes.all()

<<<<<<< HEAD

=======
>>>>>>> c42e347d (atomic transaction)
        ip_address, is_routable = get_client_ip(request)
        session_key = request.session.session_key
        user = request.user if request.user.is_authenticated else None

        if not session_key:
            request.session.create()
            session_key = request.session.session_key

<<<<<<< HEAD
        # Check if the view already exists
        if not ProductView.objects.filter(product=product, ip_address=ip_address, session_key=session_key, user=user).exists():
            ProductView.objects.create(product=product, ip_address=ip_address, session_key=session_key, user=user)



        return render(request, 'products/detail.html', {'product': product, 'form':form, 'attr':attr})
=======
        if not ProductView.objects.filter(product=product, ip_address=ip_address, session_key=session_key, user=user).exists():
            ProductView.objects.create(product=product, ip_address=ip_address, session_key=session_key, user=user)
        
        comments = product.pcomments.all()


        return render(request, 'products/detail.html', {'product': product, 'form':form, 'attr':attr, 'comments': comments})




    def post(self, request, slug):
        product = get_object_or_404(Products, slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()
            return redirect('products:detail', slug=product.slug)
        

        comments = product.pcomments.all()
        attr = product.product_attributes.all()
        cart_form = CartAddForm() 

        return render(request, 'products/detail.html', {
            'product': product,
            'form': cart_form,
            'attr': attr,
            'comments': comments,
            'comment_form': form
        })

>>>>>>> c42e347d (atomic transaction)
        





<<<<<<< HEAD

=======
>>>>>>> c42e347d (atomic transaction)
