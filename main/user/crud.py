"""
DAO (Data Access Object) file

Helper file containing functions for accessing data in our database
"""
from user.models import User
from user.models import UserRole

def create_user(user_data):
    """
    Creates and Returns given user_data
    """

    user = User( 
            phone_number = user_data.get('phone_number'),
            profile_pic = user_data.get('profile_pic'),
            background_pic = user_data.get("background_pic"),
            username = user_data.get("username"),
            password_digest = user_data.get("password"),
            firstname = user_data.get("firstname"),
            lastname = user_data.get("lastname"),
            email = user_data.get("email"),
            about = user_data.get("about")
            )
    user.save()

    #become org_contributor on creation
    #become org admin on addition or creation of org
    #become super admin ???
    user_role = UserRole(
        org_contributor = user_data.get("roles").get("organization_contributor"),
        org_admin = user_data.get("roles").get("organization_admin"),
        super_admin = user_data.get("roles").get("super_admin")
    )

    user_role.save()
    user.roles.add(user_role)

    user.save()
    print("ghsdgfhgwauerugweuirt")
    return True, user


def update_user(user_id, user_data):
    """
    Updates and Returns User given user_id and user_data
    """
    exists, user = get_user(user_id)

    if not exists:
        return False, user


    user.firstname = user_data.get('firstname')
    user.lastname = user_data.get('lastname')
    user.username = user_data.get('username')
    user.password_digest = user_data.get('password')
    user.about = user_data.get('about')
    user.email = user_data.get('email')
    user.phone_number = user_data.get('phone_number')
    user.profile_pic = user_data.get('profile_pic')
    user.background_pic = user_data.get('background_pic')

    user.save()

    return True, user

def update_user_role(user_id, user_data):
    """
    Updates user roles and Returns User given user_id and user_data
    """
    exists, user = get_user(user_id)

    if not exists:
        return False, user
    #TODO: need to reconsider this
    roles = user.roles 

    res = []
    for role in roles.all():
        role.org_contributor = user_data.get("organization_contributor")
        role.org_admin = user_data.get("organization_admin")
        role.super_admin = user_data.get("super_admin")
        role.save()
        res.append(role.serialize())


    return True, {"user_id:" : user.id, "user_roles" : res}


def delete_user(user_id):
    """
    Deletes and Returns User given user_id
    """
    exists, user = get_user(user_id)

    if not exists:
        return False, user
    
    user.is_deleted = True
    user.save()
    return True, user


def get_user(user_id):
    """
    Retrieves and Returns User given user_id
    """
    user = User.objects.get(id = user_id)

    if not user:
        return False, user
    
    return True, user

def get_users():
    """
    Retrieves and Returns User given user_id
    """
    users = User.objects.all()
    res = []

    for user in users:
        res.append(user.serialize())

    return {"users" : res}
