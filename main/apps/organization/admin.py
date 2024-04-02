from django.contrib import admin

from .models import (Category, Organization, Organization_Admin,
                     Organization_Category, Organization_File,
                     Organization_Member, Organization_Tag)

# Register your models here.
admin.site.register(Organization)
admin.site.register(Category)
admin.site.register(Organization_Admin)
admin.site.register(Organization_Member)
admin.site.register(Organization_Category)
admin.site.register(Organization_Tag)
admin.site.register(Organization_File)
