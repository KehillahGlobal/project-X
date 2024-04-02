from django.contrib import admin

from .models import Role, User, User_File, User_Role, User_Tag

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(User_Role)
admin.site.register(User_Tag)
admin.site.register(User_File)
