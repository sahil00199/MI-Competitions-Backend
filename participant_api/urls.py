from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^participant/(?P<mi_number>MI-[A-Z]{3}-[0-9]+)', views.ParticipantDetail.as_view()),
    url(r'^participant/', views.CreateParticipant.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)