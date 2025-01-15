from django.urls import path
from users.views import register_view, login_view, confirm_email

app_name = 'users'

urlpatterns = [
    path('', register_view, name='register'), 
    path('login/', login_view, name='login'),  
    path('confirm/email/<str:uid>/<str:token>/', confirm_email, name='confirm_email'), 
]
