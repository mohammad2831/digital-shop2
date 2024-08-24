from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('products/', include('products.urls', namespace='products')),
    path('accounts/', include('accounts.urls', namespace='accountss')),
    path('orders/', include('orders.urls', namespace='orders')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)