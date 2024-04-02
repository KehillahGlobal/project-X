from apps.user.models import User, User_Role


def create_user(user_data):
    """
    Creates and Returns given user_data
    """

    user = User(
        phone_number=user_data.get("phone_number"),
        profile_pic=user_data.get("profile_pic"),
        background_pic=user_data.get("background_pic"),
        username=user_data.get("username"),
        password_digest=user_data.get("password"),
        firstname=user_data.get("firstname"),
        lastname=user_data.get("lastname"),
        email=user_data.get("email"),
        about=user_data.get("about"),
    )

    # become org_contributor on creation
    # become org admin on addition or creation of org
    # become super admin ???
    user_role = User_Role()

    user_role.save()
    user.roles.add(user_role)
    user.save()

    return user


def update_user(user_id, user_data):
    """
    Updates and Returns User given user_id and user_data
    """
    user = get_user(user_id)

    if user:
        user.firstname = user_data.get("firstname")
        user.lastname = user_data.get("lastname")
        user.username = user_data.get("username")
        user.password_digest = user_data.get("password")
        user.about = user_data.get("about")
        user.email = user_data.get("email")
        user.phone_number = user_data.get("phone_number")
        user.profile_pic = user_data.get("profile_pic")
        user.background_pic = user_data.get("background_pic")

        user.save()

    return user


def update_user_role(user_id, user_data):
    """
    Updates user roles and Returns User given user_id and user_data
    """
    user = get_user(user_id)

    if not exists:
        res = []
        roles = user.roles
        for role in roles.all():
            role.org_contributor = user_data.get("organization_contributor")
            role.org_admin = user_data.get("organization_admin")
            role.super_admin = user_data.get("super_admin")
            role.save()
            res.append(role.serialize())

        return {"user_id:": user.id, "user_roles": res}
    return {}


def delete_user(user_id):
    """
    Deletes and Returns User given user_id
    """
    user = get_user(user_id)

    if user:
        user.is_deleted = True
        user.save()
    return user


def get_user(user_id):
    """
    Retrieves and Returns User given user_id
    """
    return User.objects.get(id=user_id)


def get_users():
    """
    Retrieves and Returns User given user_id
    """
    users = User.objects.all()
    res = []

    for user in users:
        res.append(user.serialize())

    return {"users": res}
