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
    url('^events', views.Event),
    url('^events/actors/<int:pk>'),
    url('^actors'),
    url('^repos')

]

urlpatterns = format_suffix_patterns(urlpatterns)
