from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^pronites/$', views.Pronite1.as_view()),
    url(r'^pronites/genres/$', views.PronitesGenreList.as_view()), #list of all genres
    url(r'^pronites/genre/(?P<genre_id>[0-9]+)/$', views.PronitesGenre1.as_view()), #info on one genre
    url(r'^pronites/event/(?P<event_id>[0-9]+)/$', views.PronitesEvent1.as_view()),#info on one event
    url(r'^pronites/events/(?P<genre_id>[0-9]+)/$', views.PronitesEventList.as_view()),#all events under a genre
]

urlpatterns = format_suffix_patterns(urlpatterns)