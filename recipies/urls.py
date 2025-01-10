from django.urls import path

from recipies.views import recipies_list_view,recipies_category_list_view

app_name = 'recipies'

urlpatterns = [
    path('category/',recipies_category_list_view,name='category'),
    path('',recipies_list_view,name='list'),

]