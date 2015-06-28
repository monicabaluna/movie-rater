from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.list_movies),
    url(r'^add_movie$', views.add_movie),
]