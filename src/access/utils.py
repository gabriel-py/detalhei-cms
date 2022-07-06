from django.utils.text import slugify
from .models import Menu


def _parent_allowance(parents, routes, path, allowed):
    route = "/".join(path.split("/")[:-1]) or path

    if route not in parents:
        return allowed

    parent = parents[route]
    if parent["allowed"]:
        return True

    if allowed:
        if not [r for r in routes if r["path"] == parent["path"]]:
            routes.append(parent)
        return True

    return False

def get_routes(user):
    routes = []
    usergroups = [g.id for g in user.groups.all()]
    menus = Menu.objects.filter(enabled=True).order_by("path")
    parents = {}

    for menu in menus:
        route = {
            "path": menu.path,
        }

        allowed = user.is_superuser or menu.groups.filter(id__in=usergroups).count()

        if menu.menu_type in ["MODULE", "MENU"]:
            parents[menu.path] = route
            parents[menu.path]["allowed"] = True

            if not allowed:
                parents[menu.path]["allowed"] = False
                continue

            routes.append(route)
            continue

        if _parent_allowance(parents, routes, route["path"], allowed):
            routes.append(route)

    return routes
