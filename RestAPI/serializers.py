# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Event, Actor, Repo


class ActorSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Actor
        fields = '__all__'


class RepoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Actor
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    repo = RepoSerializer(many=True, read_only=True)
    actor = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'

