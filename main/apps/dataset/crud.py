from datetime import datetime

from apps.dataset.models import (Dataset, DatasetBookmark, DatasetComment,
                                 DatasetFile, DatasetLike, DatasetMetadata,
                                 DatasetTag)
from apps.organization.crud import get_org
from apps.user.models import User
from utils.errors import (CommentDoesNotExist, DatasetDoesNotExist,
                          UserDoesNotExist, UserNotAuthorized)


def create_dataset(data, user_id: int):
    """
    Creates dataset with `data` and sets user `user_id` as the author.
    """
    author = User.objects.filter(id=user_id).first()
    if not author:
        raise UserDoesNotExist

    dataset = Dataset(author=author)
    for field in Dataset.custom_single_fields:
        setattr(dataset, field, data.get(field))

    dataset.metadata = create_dataset_metadata(user_id, data)
    dataset.save()

    if files := data.get("files"):
        for file in files:
            create_dataset_file(user_id, dataset.id, file)

    if tags := data.get("tags"):
        for tag in tags:
            create_dataset_tags(user_id, dataset.id, tag)

    return {"dataset": dataset.serialize()}


def read_dataset(dataset_id):
    """
    Retrieves and Returns dataset given dataset_id
    """
    dataset = Dataset.objects.get(id=dataset_id)
    if not dataset:
        raise DatasetDoesNotExist
    return {"dataset": dataset.serialize()}


def read_all_datasets():
    """
    Retrieves and Returns all datasets
    """
    return {
        "datasets": [
            dataset.serialize()
            for dataset in Dataset.objects.filter(is_deleted=False).all()
        ]
    }


def update_dataset(dataset_id, data):
    dataset = Dataset.objects.get(id=dataset_id)
    if not dataset:
        return None

    for field in Dataset.single_fields:
        setattr(dataset, field, data.get(field))

    dataset.save()
    return {"dataset": dataset}


def delete_dataset(dataset_id):
    dataset = Dataset.objects.get(id=dataset_id)
    if not dataset:
        return None

    dataset.is_deleted = True
    dataset.save()
    dataset = Dataset.objects.get(id=dataset_id)
    return {"dataset": dataset}


def create_dataset_metadata(user_id, data):
    """
    Create metadata for dataset using `data`.
    """
    date_created = date_modified = datetime.now()
    file = data.get("metadata_file")  # * Upload to S3 and store link here

    metadata = DatasetMetadata(
        file=file,
        publisher=user_id,
        date_created=date_created,
        date_modified=date_modified,
        source_link=data.get("metadata_source_link"),
        resource_type=data.get("resource_type"),
        license_link=data.get("license_link"),
    )

    metadata.save()
    return metadata


def update_dataset_metadata(dataset_id, data):
    dataset = Dataset.objects.get(id=dataset_id)
    if not dataset:
        return None

    metadata = dataset.metadata
    if file_data := data.get("file"):
        metadata.file = create_dataset_file(dataset.author.id, dataset_id, file_data)

    for field, value in DatasetMetadata.custom_fields:
        setattr(metadata, field, value)

    metadata.date_modified = datetime().now()
    metadata.save()
    dataset.save()
    return {"dataset": dataset}


def create_comment(dataset_id, user_id, data):
    """
    Creates and Returns comment by user
    """
    owner = User.objects.get(id=user_id)
    dataset = Dataset.objects.get(id=dataset_id)
    if not (owner and dataset):
        return None

    comment = DatasetComment(dataset=dataset, author=owner, body=data.get("message"))
    comment.save()

    return {"comment": comment.serialize()}


def update_comment(comment_id, data):
    """
    Update comment with id `comment_id`.
    """
    comment = DatasetComment.objects.get(id=comment_id)
    if not comment:
        raise CommentDoesNotExist

    if body := data.get("message") != "":
        comment.body = body
        comment.save()
        return {"comment": comment.serialize()}
    return delete_comment(comment.author, comment_id)


def delete_comment(user_id, comment_id):
    """
    Deletes comment with id `comment_id`.
    """
    comment = DatasetComment.objects.filter(id=comment_id).first()
    if comment.author != user_id:
        return UserNotAuthorized
    comment.active = False
    comment.save()
    return comment.serialize()


def create_dataset_file(user_id, dataset_id, data):
    dataset = Dataset.objects.get(id=dataset_id)
    uploader = User.objects.get(id=user_id)
    url = data.get("url")  # * from S3

    file = DatasetFile(
        title=data.get("title"),
        url=url,
        uploader=uploader,
    )

    file.save()
    return file


def delete_file(user_id, file_id):
    file = DatasetFile.objects.filter(id=file_id).first()
    if file.owner_user.id != user_id:
        return file.serialize()
    file.active = False
    file.save()
    return file.serialize()


def create_dataset_tags(user_id, dataset_id, tag):
    """Create a `tag` for dataset `dataset_id` with user `user_id` as the author."""
    tag = DatasetTag(name=tag, dataset_id=dataset_id)
    tag.save()


def delete_tag(tag_id):
    """ """
    ...


def create_like(dataset_id, user_id, data):
    """
    User `user_id` likes or unlikes dataset `dataset_id`.
    """
    author = User.objects.get(id=user_id)
    dataset = Dataset.objects.get(id=dataset_id)
    if not (author and dataset):
        return None

    like = DatasetLike(dataset=dataset, author=author, body=data.get("message"))
    like.save()

    return {"comment": like.serialize()}


def delete_like(like_id, user_id):
    """
    Deletes and Returns like by user
    """
    like = DatasetLike.objects.get(id=like_id)
    if like_id.owner_user.id != user_id:
        return like

    like.active = False
    like.save()

    return like.serialize()


def create_bookmark(user_id, bookmark_data):
    """
    Creates and Returns bookmark by user
    """
    dataset = dataset = read_dataset(bookmark_data.get("dataset_id"))
    user = User.objects.get(id=user_id)
    bookmark = DatasetBookmark.objects.filter(
        owner_user=user, dataset=dataset, status=True
    ).first()

    if bookmark:
        return bookmark

    bookmark = DatasetBookmark(user=user, dataset=dataset)
    bookmark.save()
    return bookmark


def delete_bookmark(user_id, bookmark_id):
    """
    Deletes and Returns bookmark by user
    """

    bookmark = DatasetBookmark.objects.filter(id=bookmark_id).first()
    if bookmark_id.owner_user.id != user_id:
        return bookmark
    bookmark.status = False
    bookmark.save()

    return bookmark.serialize()


def add_owner_org(user_id, dataset_data):
    """
    Adds owner org to dataset by user
    """
    dataset = read_dataset(dataset_data.get("dataset_id"))
    org = get_org(dataset_data.gete("org_id"))

    if dataset.owner_user.id != user_id:
        return dataset
    dataset.owner_org = org
    dataset.save()

    return dataset  # TODO: remove owner org or just update


def publish_dataset(user_id, dataset_id):
    """
    Publishes dataset by user
    """
    dataset = read_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return dataset

    dataset.is_published = True
    dataset.save()

    return dataset


def unpusblish_dataset(user_id, dataset_id):
    """
    Unpublishes dataset by user
    """
    dataset = read_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return dataset

    dataset.is_published = False
    dataset.save()

    return dataset


def archive_dataset(user_id, dataset_id):
    """
    Archives dataset by user
    """
    dataset = read_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return dataset

    dataset.is_archived = True
    dataset.save()

    return dataset


def unarchive_dataset(user_id, dataset_id):
    """
    Unarchives dataset by user
    """
    dataset = read_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return dataset

    dataset.is_archived = False
    dataset.save()

    return dataset


def approve_dataset(user_id, dataset_id):
    """
    Approves dataset by user
    """
    dataset = read_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return dataset

    dataset.is_approved = True
    dataset.save()

    return dataset


def disapprove_dataset(user_id, dataset_id):
    """
    Disapproves dataset by user
    """
    dataset = read_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return dataset

    dataset.is_approved = False
    dataset.save()

    return dataset


# TODO: if depends on condition, use tuple returns else return serialized()
