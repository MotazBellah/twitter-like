from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view),
    path('tweets', views.tweet_list_view),
    path('tweets/<int:tweet_id>', views.home_detail_view),
]
