from django.urls import path
from .views import *

urlpatterns = [
    path('post-list/', post_list),
    path('post-create/', post_create),
    path('update-post/<str:post_url>/', update_post),
    path('delete-post/<str:post_url>/', post_delete),
    path('company-list/', company_list),
    path('list-vacancy/', list_vacancy),
    path('vacancy/<slug:vacancy_slug>/', detail_vacancy),
    path('mentor-list/', list_mentors),
    path('mentor-update/', update_mentor),
    path('create-mentor/', create_mentor)
]
