"""Serializers for Task model."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Task model serializer."""

    class Meta:
        """Serializer metadata."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
