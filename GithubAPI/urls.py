from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic.base import RedirectView
from RestAPI import views

from RestAPI import views

urlpatterns = [
    # Dummy route. Can be removed.
    url(r'^/', RedirectView.as_view(url='https://hackerrank.com', permanent=False)),
]
urlpatterns += [
    url(r'^events', views.ListCreateEvent.as_view()),
    url(r'^events/(?P<id>[0-9]+)/$', views.RetrieveUpdateDestroyEvent.as_view()),
    url(r'^events/actors/(?P<id>[0-9]+)/$', views.RetrieveUpdateDestroyEvent.as_view()),
    url(r'^actors', views.ListCreateActor.as_view()),
    url(r'^actors/(?P<id>[0-9]+)/$', views.RetrieveUpdateDestroyActor.as_view()),
    url(r'^repos', views.ListCreateRepo.as_view()),
    url(r'^repos/(?P<id>[0-9]+)/$', views.RetrieveUpdateDestroyRepo.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
