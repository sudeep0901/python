from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
u = User.objects.create_user(username='djsudeep')
u.has_perm('auth.change_user')
su = User.objects.create_superuser(
    username='susudeep', email='sudeep.m.patel@gmail.com', password='secret',)
su.has_perm('does.not.exist')


def users_list_view(request):
    if not request.user.has_perm('auth.view_user'):
        raise PermissionDenied()


@permission_required('auth.view_user')
def users_list_view(request):
    pass
