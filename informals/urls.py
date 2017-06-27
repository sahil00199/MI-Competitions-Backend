from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^informals/$', views.Informal1.as_view()),
    url(r'^informalsGenres/$', views.InformalsGenreList.as_view()), #list of all genres
    url(r'^informalsGenre/(?P<genre_id>[0-9]+)/$', views.InformalsGenre1.as_view()), #info on one genre
    url(r'^informalsEvent/(?P<event_id>[0-9]+)/$', views.InformalsEvent1.as_view()),#info on one event
    url(r'^informalsEvents/(?P<genre_id>[0-9]+)/$', views.InformalsEventList.as_view()),#all events under a genre
]

urlpatterns = format_suffix_patterns(urlpatterns)