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
    url(r'^events/$', views.ListCreateEvent.as_view(), name='event-list'),
    url(r'^erase/$', views.destroy_event),
    url(r'^events/actors/(?P<actor>.+)/$', views.RetrieveUpdateDestroyEvent.as_view(), name='event-detail'),
    url(r'^actors/$', views.ListCreateActor.as_view(), name='actor-list'),
    url(r'^actors/streak/$', views.get_streak, name='actor-detail'),
    url(r'^actors/(?P<pk>[0-9]+)/$', views.RetrieveUpdateDestroyActor.as_view(), name='actor-detail'),
    url(r'^repos/$', views.ListCreateRepo.as_view(), name='repo-list'),
    url(r'^repos/(?P<id>[0-9]+)/$', views.RetrieveUpdateDestroyRepo.as_view(), name='repo-detail')

]

urlpatterns = format_suffix_patterns(urlpatterns)
