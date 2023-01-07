from django import template

from tree_menu_app.models import MenuItem

register = template.Library()


@register.inclusion_tag('tree_menu_app/menu.html')
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(name=menu_name)
    return {'menu_items': menu_items}
