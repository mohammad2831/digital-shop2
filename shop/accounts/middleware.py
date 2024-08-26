from django.core.exceptions import PermissionDenied
from .models import AdminLock

class AdminLockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.process_request(request)
        if response is None:
            response = self.get_response(request)
        return response

    def process_request(self, request):
        if request.user.is_authenticated and request.user.is_superuser:
            if AdminLock.objects.exists() and not AdminLock.objects.filter(user=request.user).exists():
                raise PermissionDenied("Another admin is currently editing. Please wait.")
