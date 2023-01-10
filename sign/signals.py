from django.dispatch import receiver
from django.contrib.auth.models import Group
from registration.signals import user_registered
from django.contrib.auth.models import User


@receiver(user_registered, sender=User)
def user_registered_callback(sender, user, request, **kwargs):
    print('yes')
    group_name = request.POST['group_id'] or None
    if group_name:
        try:
            g = Group.objects.get(name='common')
        except Group.DoewNotExists:
            g = None

        if g:
            g.user_set.add(user)