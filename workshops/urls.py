from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^workshops/$', views.Workshops.as_view()),
    #url(r'^workshops/genres/$', views.WorkshopsGenreList.as_view()), #list of all genres
    #url(r'^workshops/genre/(?P<genre_id>[0-9]+)/$', views.WorkshopsGenre1.as_view()), #info on one genre
    #url(r'^workshops/event/(?P<event_id>[0-9]+)/$', views.WorkshopsEvent1.as_view()),#info on one event
    #url(r'^workshops/events/(?P<genre_id>[0-9]+)/$', views.WorkshopsEventList.as_view()),#all events under a genre
]

urlpatterns = format_suffix_patterns(urlpatterns)