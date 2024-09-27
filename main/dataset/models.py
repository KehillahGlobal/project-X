from django.db import models

# Create your models here.


class Dataset(models.Model):
    """
    Dataset model
    """
    is_verified = models.BooleanField(default= False)
    has_user_policy = models.BooleanField(default=False)
    is_government = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)


    is_published = models.BooleanField(default=False)
    is_archived = models.BooleanField(default= True)
    is_approved = models.BooleanField(default=False)

    title = models.CharField(max_length= 100, default="")  

    description = models.CharField(max_length= 1000, default="")  

    status = models.TextField(default=None)  #make it choices

    addt_info = models.TextField(default=None)

    is_deleted = models.BooleanField(default=False)

    owner_organization = models.ForeignKey("organization.Organization", on_delete=models.RESTRICT, null=True)
    owner_user = models.ForeignKey("user.User", on_delete=models.RESTRICT, default=None)


    dataset_metadata = models.ForeignKey("DatasetMetadata", on_delete=models.RESTRICT, default=None, unique= True, null=True)

    # TODO:multiple serialize

    def serialize(self):
        """
        Serializes a Dataset object
        """
        return {
            "id" : self.id,
            "is_verified" : self.is_verified,
            "has_user_policy" : self.has_user_policy,
            "is_government" : self.is_government,
            "is_public" : self.is_public,
            "is_published" : self.is_published,
            "is_archived" : self.is_archived,
            "is_approved" : self.is_approved,
            "title": self.title,
            "description": self.description,
            "status" : self.status,
            "is_deleted" : self.is_deleted,
            "addt_info" : self.addt_info,
            "owner_user" : self.owner_user.serialize() if self.owner_user else None,
            "owner_organization" : self.owner_organization.serialize() if self.owner_organization else None,
            "dataset_metadata" : self.dataset_metadata.serialize(),
        }
 


class File(models.Model):
    """
    File model
    """
    title = models.CharField(max_length=50)
    file_url = models.CharField(max_length=50, default= None)

    owner_user = models.ForeignKey("user.User", on_delete=models.RESTRICT, null=True, related_name= "user_files")
    dataset = models.ForeignKey("Dataset", on_delete=models.RESTRICT, null=True, related_name="dataset_files")
    owner_org = models.ForeignKey("organization.Organization", on_delete=models.RESTRICT, null=True, related_name="org_files")
    status = models.BooleanField(default=True)

    def serialize(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "file_url" : self.file_url,
            "status" : self.status,
            "owner_user" : self.owner_user.id if self.owner_user else None
        }

# TODO: consider situation where orgs and users are also tagged
# TODO: name and type of that tag
# TODO: users, organizations should have files as well/relationships
# TODO: likes table 


class Tag(models.Model):
    """
    Dataset Tag model
    """
    name = models.CharField(max_length=50)
    user = models.ForeignKey("user.User", on_delete=models.RESTRICT, null=True)
    dataset = models.ForeignKey("Dataset", on_delete=models.RESTRICT, null=True)
    org = models.ForeignKey("organization.Organization", on_delete=models.RESTRICT, null=True)

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name
        }


class Comment(models.Model):
    """
    Dataset Comment model
    """
    dataset = models.ForeignKey("Dataset", on_delete=models.RESTRICT)
    owner_user = models.ForeignKey("user.User", on_delete=models.RESTRICT)
    body = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def serialize(self):
        return {
            "id" : self.id,
            "body" : self.body,
            "dataset" : self.dataset.id if self.dataset else None,
            "owner_user" : self.owner_user.id if self.owner_user else None,
            "status" : self.status
        }


class DatasetMetadata(models.Model):
    """
    Dataset Metadata model
    """
    metadata_file = models.CharField(max_length= 50, null=True)  #relation with file model
    metadata_blurb = models.CharField(max_length= 1000, blank= True, null= True)
    metadata_source_link = models.URLField()
    metadata_resource_type = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)  # user or org or Admin ?
    maintainer = models.CharField(max_length=100)  # user or org or Admin ?
    license_link = models.URLField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)


    def serialize(self):
        return {
            "id" : self.id,
            "metadata_file" : self.metadata_file,
            "date_created" : self.date_created,
            "date_modified" : self.date_modified
        }
    

class Like(models.Model):
    """
    Like model
    """
    owner_user = models.ForeignKey("user.User", on_delete=models.RESTRICT) 
    dataset = models.ForeignKey("Dataset", on_delete=models.RESTRICT)
    status = models.BooleanField(default=True)

class Bookmark(models.Model):
    """
    Bookmark model
    """

    owner_user = models.ForeignKey("user.User", on_delete=models.RESTRICT) 
    dataset = models.ForeignKey("Dataset", on_delete=models.RESTRICT)
    status = models.BooleanField(default=True)

