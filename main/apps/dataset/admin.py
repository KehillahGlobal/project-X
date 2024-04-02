from django.contrib import admin

from .models import (Dataset, DatasetBookmark, DatasetComment, DatasetFile,
                     DatasetLike, DatasetMetadata, DatasetTag,
                     RelDatasetDatasetFile, RelDatasetDatasetTag)

# Register your models here.
admin.site.register(Dataset)
admin.site.register(DatasetFile)
admin.site.register(RelDatasetDatasetFile)
admin.site.register(DatasetComment)
admin.site.register(DatasetMetadata)
admin.site.register(DatasetLike)
admin.site.register(DatasetBookmark)
admin.site.register(RelDatasetDatasetTag)
admin.site.register(DatasetTag)
