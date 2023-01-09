from django.shortcuts import render

from tree_menu_app.models import MenuItem


def tree_menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'tree_menu_app/tree_menu.html', {'menu_items': menu_items})


def main_page(request):
    return render(request, 'tree_menu_app/index.html')
