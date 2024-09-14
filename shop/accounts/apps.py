from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
<<<<<<< HEAD
=======

    def ready(self):
        import accounts.signals
>>>>>>> c42e347d (atomic transaction)
