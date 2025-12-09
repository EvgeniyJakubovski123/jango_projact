from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Comment  # модель коментаря


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    # Група Автор
    author_group, created = Group.objects.get_or_create(name='Author')
    if created:
        # Додаємо права для створення/редагування/видалення своїх коментарів
        permissions = [
            Permission.objects.get(codename='add_comment'),
            Permission.objects.get(codename='change_comment'),
            Permission.objects.get(codename='delete_comment'),
        ]
        author_group.permissions.set(permissions)

    moderator_group, created = Group.objects.get_or_create(name='Moderator')
    if created:
        permissions = list(author_group.permissions.all())
        delete_any_comment_permission = Permission.objects.get(codename='delete_comment')
        permissions.append(delete_any_comment_permission)
        moderator_group.permissions.set(permissions)
