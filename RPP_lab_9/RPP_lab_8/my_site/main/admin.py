from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *

User = get_user_model()

@admin.register(User)
class UserAdmin(UserAdmin):
    pass

admin.site.register(Users)
admin.site.register(Topics)
admin.site.register(Posts) 
admin.site.register(Authors)

