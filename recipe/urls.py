from django.urls import path


from . import views

app_name = 'recipe'

urlpatterns = [
    path('',views.home_page,name='home'),
    path('about/',views.about_page_view,name='about' ),
    path('contact/',views.contact_page_view,name='contact'),
   
]


