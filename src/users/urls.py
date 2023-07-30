from django.urls import path
from .views import *


urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('login/', AuthUser.as_view()),
    path('logout/', UserLogout.as_view()),
    path('profile/', user_profile),
    path('profile-update/', profile_update)
]
