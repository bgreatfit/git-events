# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count, Sum
from rest_framework import viewsets, permissions, generics, status

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import ActorSerializer, RepoSerializer,EventSerializer
from .models import Actor, Repo, Event


@api_view(['GET'])
def get_streak(request):
    actor = Actor.objects.annotate(sum_created_at=Sum('event.created_at')) \
        .order_by('-sum_created_at').order_by('-created_at').order_by('login')
    return Response(data=actor, status=status.HTTP_200_OK)


class ListCreateActor(generics.ListCreateAPIView):
    serializer_class = ActorSerializer

    def get_queryset(self):

        return Actor.objects.annotate(num_event=Count('event'))\
            .order_by('-num_event').order_by('-created_at').order_by('login')


class RetrieveUpdateDestroyActor(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActorSerializer

    def get_queryset(self):
        return Actor.objects.all()



class ListCreateRepo(generics.ListCreateAPIView):
    serializer_class = RepoSerializer

    def get_queryset(self):
        return Repo.objects.all()


class RetrieveUpdateDestroyRepo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RepoSerializer

    def get_queryset(self):
        return Repo.objects.all()


class ListCreateEvent(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()


class RetrieveUpdateDestroyEvent(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    lookup_field = 'actor'

    def get_queryset(self):

        queryset = Event.objects.filter(actor=self.kwargs.get('actor'))
        return queryset


@api_view(['DELETE'])
def destroy_event(request):
    event = Event.objects.all().delete()
    return Response(data={"detail": event}, status=status.HTTP_200_OK)




