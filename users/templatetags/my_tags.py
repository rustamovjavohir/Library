from django import template

register = template.Library()


def check_for_group(user, args: str):
    group: list = args.split(',')
    for gr in group:
        if user.groups.filter(name=gr).exists():
            return True
    return False


@register.filter
def has_role(user, args):
    return check_for_group(user, args)
