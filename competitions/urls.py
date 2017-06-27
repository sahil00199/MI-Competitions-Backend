from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns=[
    url(r'^individual/competition/(?P<event_id>[0-9]+)/$', views.IndividualCompetition.as_view()),
    #return event info(get request), or add participants(post request with attribute participant
    #having mi number as string)

    url(r'^individual/user/(?P<mi_number>MI-[A-Z]{3}-[0-9]+)/$', views.IndividualEventsForUser.as_view()),
    #return all individual events for user with given mi number registered for

    url(r'^group/competition/(?P<event_id>[0-9]+)/$', views.GroupCompetition.as_view()),
    #return event info(get request), or add a participant group(post request with attributes name-
    #name of group and participants-list of mi numbers of those participating)
    #eg: participants='[MI-BIG-101,MI-HOT-123,MI-ASS-234]' name="Swaggy Dancers"

    url(r'^group/user/(?P<mi_number>MI-[A-Z]{3}-[0-9]+)/$', views.GroupEventsForUser.as_view()),
    #return all group events for user with given mi number

    url(r'^competitions/$', views.GeneralInfo.as_view()),#general competitions description

    url(r'^competitions/genres/$', views.AllGenres.as_view()), #return list of all genres

    url(r'^competitions/events/indiv/(?P<genre_id>[0-9]+)/$', views.IndividualEventsUnderGenre.as_view()),
    #return all the individual events under a particular genre

    url(r'^competitions/events/grp/(?P<genre_id>[0-9]+)/$', views.GroupEventsUnderGenre.as_view()),
    #returns all the group events under a particular genre

    url(r'^competitions/genre/info/(?P<genre_id>[0-9]+)/$', views.GenreInfo.as_view()),
    #return the information about a particular genre
]

urlpatterns = format_suffix_patterns(urlpatterns)