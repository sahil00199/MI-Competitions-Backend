from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^proshows/$', views.Proshows.as_view()),
    #url(r'^proshows/genres/$', views.ProshowsGenreList.as_view()), #list of all genres
    #url(r'^proshows/genre/(?P<genre_id>[0-9]+)/$', views.ProshowsGenre1.as_view()), #info on one genre
    #url(r'^proshows/event/(?P<event_id>[0-9]+)/$', views.ProshowsEvent1.as_view()),#info on one event
    #url(r'^proshows/events/(?P<genre_id>[0-9]+)/$', views.ProshowsEventList.as_view()),#all events under a genre
    #url(r'^proshows/events/all/', views.ProshowsEventAll.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)