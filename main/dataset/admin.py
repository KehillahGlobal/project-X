from django.contrib import admin
from .models import Dataset, File, Tag, Comment, DatasetMetadata, Like, Bookmark

# Register your models here.


admin.site.register(Dataset)
admin.site.register(File)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(DatasetMetadata)
admin.site.register(Bookmark)