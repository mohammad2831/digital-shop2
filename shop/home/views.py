from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse

from products.models import Category_Type, Category_Company, Products,Attribute, ProductAttribute


class HomeView(View):
    def get(self, request):
        types = Category_Type.objects.all()
        return render(request, 'home/home.html', {'types': types})

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
    









def products_by_attribute_value(request, attribute_id, value):
    # دریافت مقادیر یکتا از ProductAttribute
  
    attribute_values = ProductAttribute.objects.filter(attribute_id=attribute_id, value=value).distinct()
    
    # فیلتر کردن محصولات بر اساس مقادیر attribute_values
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