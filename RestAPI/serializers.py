# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Event, Actor, Repo


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'login', 'avatar_url')


class RepoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repo
        fields = ('id', 'name', 'url')


class EventSerializer(serializers.ModelSerializer):
    repos = RepoSerializer()
    actors = ActorSerializer()

    class Meta:
        model = Event
        fields = ('id', 'type', 'created_at', 'repos', 'actors')

    def create(self, validated_data):
        print(validated_data)
        actors_data = validated_data.pop('actors')
        repos_data = validated_data.pop('repos')
        event = Event.objects.create(**validated_data)
        Actor.objects.create(**actors_data)
        Repo.objects.create(**repos_data)
        return event



