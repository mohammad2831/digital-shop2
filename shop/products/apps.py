from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
<<<<<<< HEAD
=======

    def ready(self):
        import products.signals  
>>>>>>> c42e347d (atomic transaction)
