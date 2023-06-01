

# from django.contrib.auth.decorators import user_passes_test

# def group_required(group_name):
#     def decorator(view_func):
#         @user_passes_test(lambda user: user.groups.filter(name=group_name).exists())
#         def wrapper(request, *args, **kwargs):
#             return view_func(request, *args, **kwargs)
#         return wrapper
#     return decorator

from django import templatetags
register = templatetags.Library()

@register.filter
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()