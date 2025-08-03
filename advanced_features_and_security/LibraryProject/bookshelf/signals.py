from django.apps import apps
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def setup_groups_and_permissions(sender, **kwargs):
    if sender.name != 'advanced_features_and_security':
        return

    Document = apps.get_model('advanced_features_and_security', 'Document')

    permissions = {
        "can_view": Permission.objects.get(codename="can_view"),
        "can_create": Permission.objects.get(codename="can_create"),
        "can_edit": Permission.objects.get(codename="can_edit"),
        "can_delete": Permission.objects.get(codename="can_delete"),
    }

    groups = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_create", "can_edit"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"]
    }

    for group_name, perms in groups.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm_code in perms:
            group.permissions.add(permissions[perm_code])
