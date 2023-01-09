from django.urls import path

from tree_menu_app import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('tree-menu/', views.tree_menu, name='tree_menu'),
]
