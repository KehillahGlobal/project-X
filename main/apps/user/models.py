from django.db import models


# Create your models here.
class User(models.Model):
    """
    User model
    """

    phone_number = models.CharField(max_length=50, null=True)
    profile_pic = models.CharField(
        max_length=100, blank=True, null=True
    )  # TODO:filed fields are not serializable
    background_pic = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, null=True)
    password_digest = models.CharField(max_length=50, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True, unique=True)
    about = models.CharField(max_length=1000, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    roles = models.ManyToManyField("Role", through="User_Role")
    tags = models.ManyToManyField("dataset.DatasetTag", through="User_Tag")
    files = models.ManyToManyField("dataset.DatasetFile", through="User_File")

    def serialize(self):
        return {
            "id": self.id,
            "phone_number": self.phone_number,
            "profile_picture": self.profile_pic,
            "background_picture": self.background_pic,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "about": self.about,
            "is_deleted": self.is_deleted,
            "bookmarks": [
                bookmark.serialize() for bookmark in self.user_bookmarks.all()
            ],
            "likes": [like.serialize() for like in self.user_likes.all()],
            "comments": [
                comment.serialize()
                for comment in self.user_comments.all()
                if comment.active
            ],
            "roles": [role.serialize() for role in self.roles.all()],
            "tags": [tag.serialize() for tag in self.tags.all()],
            "files": [file.serialize() for file in self.files.all()],
        }


class Role(models.Model):
    """
    Role model
    """

    name = models.CharField(max_length=20, default="PROFILE_USER")

    def serialize(self):
        return {"id": self.id, "role": self.name}


class User_Role(models.Model):
    users = models.ForeignKey(User, on_delete=models.RESTRICT, default=None)
    roles = models.ForeignKey(Role, on_delete=models.RESTRICT, default=None)


class User_Tag(models.Model):
    tags = models.ForeignKey("dataset.DatasetTag", on_delete=models.RESTRICT)
    users = models.ForeignKey("User", on_delete=models.RESTRICT)


class User_File(models.Model):
    files = models.ForeignKey("dataset.DatasetFile", on_delete=models.RESTRICT)
    users = models.ForeignKey("User", on_delete=models.RESTRICT)
