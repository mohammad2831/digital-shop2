from django.urls import path
from . import views

app_name= 'products'
urlpatterns =[
    path('all/', views.AllView.as_view(), name='all'),
    path('detail/<slug:slug>/', views.DetailProductView.as_view(), name='detail')
]