from apps.organization.models import Organization
from apps.user.crud import get_user


def create_org(org_data, admin_id):
    """
    Creates and Returns Organization given org_data
    """
    success, admin = get_user(admin_id)

    if not success:
        return None

    org = Organization(
        organization_name=org_data.get("organization_name"),
        location=org_data.get("location"),
        address=org_data.get("address"),
        phone_number=org_data.get("phone_number"),
        email=org_data.get("email"),
        password=org_data.get("password"),
        description=org_data.get("description"),
    )

    if not success:
        return org

    org.save()
    org.admins.add(admin)

    for org_type in org_data.get("categories"):
        org_category = Category(type=org_type)
        org_category.save()
        org.categories.add(org_category)

    return True, org


def update_org(org_id, org_data):
    """
    Updates and Returns Organization given org_id and org_data
    """
    success, org = get_org(id=org_id)

    if not success:
        return org

    org.organization_name = org_data.get("organization_name")
    org.location = org_data.get("location")
    org.address = org_data.get("address")
    org.phone_number = org_data.get("phone_number")
    org.email = org_data.get("email")
    org.password = org_data.get("password")
    org.description = org_data.get("description")

    org.save()

    return True, org


def delete_org(org_id):
    """
    Deletes and Returns Organization given org_id
    """
    success, org = get_org(id=org_id)

    if not success:
        return org

    org.is_deleted = True
    org.save()

    return True, org


def get_org(org_id):
    """
    Retrieves and Returns Organization given org_id
    """
    org = Organization.objects.get(id=org_id)

    if not org:
        return org

    return True, org


def add_category(org_id):
    """ """


def remove_category(org_id):
    """ """


def add_org_member(admin_id, org_data):  # TODO: add member or members
    """
    Adds member to organization by user
    """
    member_id = org_data.get("member_id")
    success, member = get_user(member_id)
    if not success:
        return member

    success, org = get_org(org_data.get("org_id"))

    if not success:
        return member

    success, admin = get_user(admin_id)

    if not success:
        return member

    admin = org.admins.filter(admin).first()

    if not admin:
        return member

    org.members.add(member)
    # TODO: reconsider roles field for user
    org.save()

    return True, member


def remove_org_member(admin_id, org_data):
    """
    Removes member from organization by user
    """

    member_id = org_data.get("member_id")
    success, member = get_user(member_id)

    if not success:
        return member

    success, org = get_org(org_data.get("org_id"))
    if not success:
        return member

    admin = org.admins.filter(admin=get_user(admin_id)).first()

    if not admin:
        return member

    org.members.remove(member)
    org.save()

    return True, member


def approve_org():
    """
    Approve organization by user
    """


def disapprove_org():
    """
    Disapprove organization by user
    """
