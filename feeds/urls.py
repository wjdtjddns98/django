from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_feed),
    path("<int:feed_id>/<str:feed_content>", views.one_feeds),
    path("all", views.all_feeds),
]