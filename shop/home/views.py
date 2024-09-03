from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from products.models import Category_Type, Category_Company, Products,Attribute, ProductAttribute
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from products.models import Products


class HomeView(View):
    def get(self, request):
        types = Category_Type.objects.all()
        return render(request, 'home/home.html', {'types': types})
    
    def post(request):
        pass

class CompanyView(View):
    def get(self, request, slug):
        category_type = get_object_or_404(Category_Type, pk=slug)
        companies = Category_Company.objects.filter(type=category_type)
        return render(request, 'home/company.html', {'category_type': category_type, 'companies': companies})
    
class ProductFilterView(View):
    def get(self, request, slug):
        company = get_object_or_404(Category_Company, slug=slug)
        product = Products.objects.filter(category =company)
        return render(request, 'home/product_filter.html', {'company': company, 'product': product})
    


class CreateCommentView(LoginRequiredMixin, View):

    form_class = CommentForm

    def get(self, request, slug):
        product = get_object_or_404(Products, slug=slug)
        comments = product.pcomments.all()
        form = self.form_class()
        return render(request, 'products/detail.html', {'comments': comments, 'comment_form': form})
    






''' 
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug, published=True)
        form = self.form_class(request.POST)
        if form.is_valid():
            Comment.objects.create_comment(
            user = request.user,
            post = post,
            body = form.cleaned_data['body'],
            )
            messages.success(request, 'Your comment has been added.')
            return redirect('accounts:create_comment', slug=post.slug)
        comments = post.pcomments.filter(published=True)
        return render(request, 'accounts/comment.html', {'post': post, 'comments': comments, 'form': form})


'''   

















































def products_by_attribute_value(request, attribute_id, value):
  
    attribute_values = ProductAttribute.objects.filter(attribute_id=attribute_id, value=value).distinct()
    
    product = Products.objects.filter(product_attributes__in=attribute_values).distinct()
    
    return render(request, 'home/product-attr-filter.html', {'product': product, 'value':value})


def get_attributes(request, id):
    category = get_object_or_404(Category_Type, id=id)
    attributes = Attribute.objects.filter(category=category)
    attributes_data = [{'id': attr.id, 'name': attr.name} for attr in attributes]
    return JsonResponse({'attributes': attributes_data})

def get_attribute_values(request, id):
    attribute = get_object_or_404(Attribute, id=id)
    attribute_values = ProductAttribute.objects.filter(attribute=attribute).values('value').distinct()
    values_data = [{'value': value['value']} for value in attribute_values]
    return JsonResponse({'values': values_data})


