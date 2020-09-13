from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('create_upload', views.create_upload,name="create_upload"),
    path('delete_upload/<int:uid>/<int:vid>', views.delete_upload,name="delete_upload"),
    path('like_upload/<int:vid>', views.like_upload,name="like_upload"),
    path('search',views.search,name="search"),
    path('trending',views.trending,name="trending"),
    path('aboutsite',views.aboutsite,name="aboutsite"),
]