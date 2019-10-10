# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, permissions, generics, status

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import ActorSerializer, RepoSerializer,EventSerializer
from .models import Actor, Repo, Event


class ListCreateActor(generics.ListCreateAPIView):
    serializer_class = ActorSerializer

    def get_queryset(self):
        return Actor.objects.all()


class RetrieveUpdateDestroyActor(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActorSerializer

    def get_queryset(self):
        return Actor.objects.all()


class ListCreateRepo(generics.ListCreateAPIView):
    serializer_class = RepoSerializer

    def get_queryset(self):
        return Repo.objects.all()

    # def perform_create(self, serializer):
    #     user = get_object_or_404(
    #         User, pk=self.request.user.id
    #     )
    #     serializer.save(user=user, name=serializer.validated_data['name'])


class RetrieveUpdateDestroyRepo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RepoSerializer

    def get_queryset(self):
        return Repo.objects.all()


class ListCreateEvent(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        print('Hello')
        print(self.kwargs)
        return Event.objects.all()

    # def perform_create(self, serializer):
    #     user = get_object_or_404(
    #         User, pk=self.request.user.id
    #     )
    #     serializer.save(user=user, name=serializer.validated_data['name'])


class RetrieveUpdateDestroyEvent(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    lookup_field = 'actor'

    def get_queryset(self):

        queryset = Event.objects.filter(actor=self.kwargs.get('actor'))
        return queryset


