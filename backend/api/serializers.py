"""Serializers."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """TaskSerializer."""

    class Meta:
        """Class Meta."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
