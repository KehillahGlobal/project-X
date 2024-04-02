from django.db import models


# Create your models here.
class Organization(models.Model):
    """
    Organization model
    """

    name = models.CharField(max_length=100, default=None)
    location = models.CharField(max_length=100, default=None)
    address = models.CharField(max_length=100, default=None)
    phone_number = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)
    password = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=1000, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    categories = models.ManyToManyField(
        "Category", through="Organization_Category"
    )
    admins = models.ManyToManyField(
        "user.User",
        related_name="admin_organizations",
        through="Organization_Admin",
    )
    members = models.ManyToManyField(
        "user.User",
        related_name="member_organizations",
        through="Organization_Member",
    )
    tags = models.ManyToManyField(
        "dataset.DatasetTag", through="Organization_Tag"
    )
    files = models.ManyToManyField(
        "dataset.DatasetFile", through="Organization_File"
    )

    def serialize(self):
        """
        Serializes Organization object
        """
        return {
            "id": self.id,
            "organization name": self.name,
            "phone_number": self.phone_number,
            "description": self.description,
            "email": self.email,
            "location": self.location,
            "address": self.address,
            "is_deleted": self.is_deleted,
            "is_approved": self.is_approved,
            "categories": [
                category.serialize() for category in self.categories.all()
            ],
            "members": [member.serialize() for member in self.members.all()],
            "admins": [admin.serialize() for admin in self.admins.all()],
            "files": [file.serialize() for file in self.files.all()],
        }


class Category(models.Model):
    """
    Category model
    """

    type = models.CharField(max_length=50)

    def serialize(self):
        return {"id": self.id, "type": self.type}


class Organization_Category(models.Model):
    organization = models.ForeignKey("Organization", on_delete=models.RESTRICT)
    category = models.ForeignKey("Category", on_delete=models.RESTRICT)


class Organization_Admin(models.Model):
    org = models.ForeignKey("Organization", on_delete=models.RESTRICT)
    admin = models.ForeignKey("user.User", on_delete=models.RESTRICT)


class Organization_Member(models.Model):
    org = models.ForeignKey("Organization", on_delete=models.RESTRICT)
    members = models.ForeignKey("user.User", on_delete=models.RESTRICT)


class Organization_Tag(models.Model):
    tags = models.ForeignKey("dataset.DatasetTag", on_delete=models.RESTRICT)
    org = models.ForeignKey("Organization", on_delete=models.RESTRICT)


class Organization_File(models.Model):
    files = models.ForeignKey("dataset.DatasetFile", on_delete=models.RESTRICT)
    org = models.ForeignKey("Organization", on_delete=models.RESTRICT)
