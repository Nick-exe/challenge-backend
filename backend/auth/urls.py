from django.urls import path

from auth.views import login
from auth.views import logout
from auth.views import login_required


urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('login-required/', login_required),
]
