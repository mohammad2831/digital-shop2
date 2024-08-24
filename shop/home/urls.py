from django.urls import path
from . import views
from .views import get_attributes, get_attribute_values

app_name= 'home'
urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),
    path('company/<slug:slug>/', views.CompanyView.as_view(), name='company'),
    path('p-filter/<slug:slug>', views.ProductFilterView.as_view(), name='product_filter' ),
    path('get-attributes/<int:id>/', views.get_attributes, name='get_attributes'),
    path('get-attribute-values/<int:id>/', views.get_attribute_values, name='get_attribute_values'),
    path('products-by-attribute/<int:attribute_id>/<str:value>/', views.products_by_attribute_value, name='products_by_attribute'),

]