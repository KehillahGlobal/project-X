from django.contrib import admin
from .models import Organization, OrganizationCategory, Organization_Admin, Organization_Members


# Register your models here.
admin.site.register(Organization)
admin.site.register(OrganizationCategory)
admin.site.register(Organization_Admin)
admin.site.register(Organization_Members)

