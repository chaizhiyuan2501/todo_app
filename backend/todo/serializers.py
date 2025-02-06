from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.Serializer):
    """Todoシリアライズ"""

    class Meta:
        model = Todo
        fields = "__all__"
