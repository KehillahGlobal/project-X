from datetime import datetime

from django.db import models


class Dataset(models.Model):
    custom_single_fields = [
        "is_government",
        "is_public",
        "title",
        "description",
        "addt_info",
    ]
    is_verified = models.BooleanField(default=False)
    has_user_policy = models.BooleanField(default=False)
    is_government = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    title = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=1000, default="")
    status = models.CharField(default="pending", max_length=10)
    addt_info = models.TextField(default=None)

    # Foreign Key Fields
    organization = models.ForeignKey(
        "organization.Organization",
        on_delete=models.RESTRICT,
        default=None,
        null=True,
    )
    author = models.ForeignKey(
        "user.User", on_delete=models.RESTRICT, default=None
    )
    metadata = models.ForeignKey(
        "DatasetMetadata", on_delete=models.RESTRICT, unique=True, blank=False
    )

    # Many-to-Many Relationships
    tags = models.ManyToManyField("DatasetTag", through="RelDatasetDatasetTag")
    files = models.ManyToManyField(
        "DatasetFile", through="RelDatasetDatasetFile"
    )

    def serialize(self):
        return {
            "id": self.id,
            "is_verified": self.is_verified,
            "has_user_policy": self.has_user_policy,
            "is_government": self.is_government,
            "is_public": self.is_public,
            "is_published": self.is_published,
            "is_archived": self.is_archived,
            "is_approved": self.is_approved,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "is_deleted": self.is_deleted,
            "addt_info": self.addt_info,
            "author": f"{self.author.firstname} {self.author.lastname}"
            if self.author
            else "",
            "organization": self.organization.serialize()
            if self.organization
            else "",
            "metadata": self.metadata.serialize(),
            "tags": [tag.serialize() for tag in self.tags.all()],
            "files": [file.serialize() for file in self.files.all()],
            "bookmarks": [
                bookmark.serialize()
                for bookmark in self.dataset_bookmarks.all()
                if bookmark.active
            ],
            "likes": [
                like.serialize()
                for like in self.dataset_likes.all()
                if like.active
            ],
            "comments": [
                comment.serialize()
                for comment in self.dataset_comments.all()
                if comment.active
            ],
        }


class DatasetMetadata(models.Model):
    custom_fields = ["license_link", "source_link", "resource_type"]

    file = models.CharField(max_length=50, null=True)
    blurb = models.CharField(max_length=1000, blank=True, null=True)
    source_link = models.URLField(null=True)
    resource_type = models.CharField(max_length=50, null=True)
    publisher = models.CharField(
        max_length=100, null=True
    )  # user or org or Admin ?
    maintainer = models.CharField(
        max_length=100, null=True
    )  # user or org or Admin ?
    license_link = models.URLField(null=True)
    date_created = models.DateField(default=datetime.today)
    date_modified = models.DateField(auto_now=True)

    def serialize(self):
        return {
            "id": self.id,
            "file": self.file,
            "date_created": self.date_created,
            "date_modified": self.date_modified,
        }


class DatasetFile(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50, default=None, blank=False)
    active = models.BooleanField(default=True)
    is_metadata = models.BooleanField(default=False)
    uploader = models.ForeignKey(
        "user.User",
        on_delete=models.RESTRICT,
        related_name="user_dataset_files",
        default=None,
    )

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "active": self.active,
            "is_metadata": self.is_metadata,
        }


# TODO: consider situation where orgs and users are also tagged
# TODO: name and type of that tag
# TODO: users, organizations should have files as well/relationships
# TODO: likes table


class DatasetComment(models.Model):
    body = models.TextField()
    date_created = models.DateField(default=datetime.today)
    date_modified = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    dataset = models.ForeignKey(
        "Dataset",
        on_delete=models.RESTRICT,
        related_name="dataset_comments",
        default=None,
    )
    author = models.ForeignKey(
        "user.User",
        on_delete=models.RESTRICT,
        related_name="user_comments",
        default=None,
    )

    def serialize(self):
        return {
            "id": self.id,
            "body": self.body,
            "active": self.active,
            "data_created": self.date_created,
        }


class DatasetTag(models.Model):
    """
    DatasetTag model
    """

    name = models.CharField(max_length=50, unique=True)

    # TODO: consider unique together here
    def serialize(self):
        return {"id": self.id, "name": self.name}


class DatasetLike(models.Model):
    active = models.BooleanField(default=True)
    author = models.ForeignKey(
        "user.User",
        on_delete=models.RESTRICT,
        default=None,
        related_name="user_likes",
    )
    dataset = models.ForeignKey(
        "Dataset",
        on_delete=models.RESTRICT,
        related_name="dataset_likes",
        default=None,
    )

    class Meta:
        unique_together = ("author", "dataset")

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "user": self.author.id,
            "dataset": self.dataset.id,
        }


class DatasetBookmark(models.Model):
    status = models.BooleanField(default=True)
    user = models.ForeignKey(
        "user.User",
        on_delete=models.RESTRICT,
        default=None,
        related_name="user_bookmarks",
    )
    dataset = models.ForeignKey(
        "Dataset",
        on_delete=models.RESTRICT,
        related_name="dataset_bookmarks",
        default=None,
    )

    class Meta:
        unique_together = ("user", "dataset")

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "user": self.user.id,
            "dataset": self.dataset.id,
        }


class RelDatasetDatasetTag(models.Model):
    tags = models.ForeignKey("DatasetTag", on_delete=models.RESTRICT)
    datasets = models.ForeignKey("Dataset", on_delete=models.RESTRICT)


class RelDatasetDatasetFile(models.Model):
    files = models.ForeignKey("DatasetFile", on_delete=models.RESTRICT)
    datasets = models.ForeignKey("Dataset", on_delete=models.RESTRICT)
