from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

from django.utils.translation import gettext, gettext_lazy as _



# Register your models here.
class CustomUserAdmin(UserAdmin):
    # add fields those needs to be visible while adding the data in form.
    add_fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password', 
                            'is_active', 'verified','date_joined')}),
    )

admin.sites.site.register(User)

