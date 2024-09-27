from django.db import models


# Create your models here.
class User(models.Model):
    """
    User model
    """
    phone_number = models.CharField(max_length=50, null=True)
    profile_pic = models.CharField(max_length=100, blank=True, null= True)  #TODO:filed fields are not serializable
    background_pic = models.CharField(max_length=100, blank=True, null= True)
    username = models.CharField(max_length = 100, null=True)
    password_digest = models.CharField(max_length= 50, null=True)
    firstname = models.CharField(max_length= 100, null=True)
    lastname = models.CharField(max_length= 100, null=True)
    email = models.EmailField(null= True, unique=True)
    about = models.CharField(max_length= 1000, blank= True, null= True)
    is_deleted = models.BooleanField(default= False)
    roles = models.ManyToManyField("UserRole", through="User_UserRole")



    def serialize(self):

        return {
            "id":  self.id,
            "phone_number" : self.phone_number,
            "profile_picture" : self.profile_pic,
            "background_picture" : self.background_pic,
            "username" : self.username,
            "firstname" : self.firstname,
            "lastname" : self.lastname,
            "email" : self.email,
            "about" : self.about,
            "is_deleted" : self.is_deleted,
            "roles" : [role.serialize() for role in self.roles.all()]
        }  #TODO: user has just a role 


class UserRole(models.Model):
    """
    User role model
    """
    profile_user = models.BooleanField(default= True)
    org_contributor = models.BooleanField(default=False)
    org_admin = models.BooleanField(default=False)
    super_admin = models.BooleanField(default=False)

    def serialize(self):
        return {
            "id" : self.id,
            "profile_user" : self.profile_user,
            "org_contributor" : self.org_contributor,
            "org_admin" : self.org_admin,
            "super_admin" : self.super_admin
        }





#     # Add any extra fields or attributes you want for this relationship
#     # extra_field = models.CharField(max_length=100)


class User_UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    user_role = models.ForeignKey(UserRole, on_delete=models.RESTRICT)





