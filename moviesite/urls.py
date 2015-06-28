from django.conf.urls import include, url
from django.contrib import admin
from movierater import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'moviesite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.list_movies),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', include('movierater.urls')),
    url(r'^add_movie/$', views.add_movie),
    url(r'^add_movie/submit_movie/$', views.submit_movie),
    url(r'^vote_movie/(?P<movie_id>\d+)/$', views.vote_movie),
    url(r'^submit_vote/(?P<movie_id>\d+)/$', views.submit_vote),
]
