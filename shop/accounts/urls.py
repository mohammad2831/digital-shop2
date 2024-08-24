from django.urls import path
from . import views
from .views import send_test_email

app_name= 'accounts'
urlpatterns =[
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('send-test-email/', send_test_email, name='send_test_email'),
     

    ]