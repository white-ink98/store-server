from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import login, registration


app_name = 'users'

urlpatterns = [
    path('login/', login.as_view(), name='login'),
    path('registration/', registration.as_view(), name='registration'),
]
