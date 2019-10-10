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
    repo = RepoSerializer()
    actor = ActorSerializer()

    class Meta:
        model = Event
        fields = ('id', 'type', 'created_at', 'repo', 'actor')

    def create(self, validated_data):
        print(validated_data)
        actors_data = validated_data.pop('actor')
        repos_data = validated_data.pop('repo')
        actor = Actor.objects.create(**actors_data)
        repo = Repo.objects.create(**repos_data)
        event = Event.objects.create(**validated_data, actor=actor, repo=repo)
        return event



