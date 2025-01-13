# from django.contrib.auth.signals import user_logged_in, user_logged_out
# from django.dispatch import receiver
# from .models import CustomUser


# @receiver(user_logged_in)
# def set_user_active_on_login(sender, request, user, **kwargs):
#     user.is_active = True
#     user.save()


# @receiver(user_logged_out)
# def set_user_inactive_on_logout(sender, request, user, **kwargs):
#     if user:
#         user.is_active = False
#         user.save()
