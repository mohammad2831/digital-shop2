from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User
from .forms import UserChangeForm, UserCreationForm

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display= ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets=(
        ('Main',{'fields':('email', 'phone_number', 'username', 'password')}),
<<<<<<< HEAD
        ('Permision',{'fields':('is_active', 'is_admin', 'is_superuser','last_login', 'user_permissions')}),
=======
        ('Permision',{'fields':('is_active', 'is_admin', 'is_superuser','last_login')}),
>>>>>>> c42e347d (atomic transaction)
    )

    add_fieldsets = (
        (None,{'fiels':('email', 'phone_number', 'username', 'password1', 'password2')}),
    )

    search_fields= ('email', 'phone_number')
    ordering = ('email', )
<<<<<<< HEAD
    filter_horizontal =('user_permissions',)
    list_per_page=3
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
=======
    filter_horizontal =()
    
    list_per_page=3
admin.site.unregister(Group)
admin.site.register(User)
>>>>>>> c42e347d (atomic transaction)
