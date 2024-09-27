from django.contrib import admin
from .models import User, UserRole
# from .models import Organization_AdminUser, Dataset_DatasetFile, Dataset_DatasetTag, Organization_OrganizationCategory, User_UserRole

# Register your models here.

admin.site.register(User)
admin.site.register(UserRole)





