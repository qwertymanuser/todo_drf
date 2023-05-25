from rest_framework import serializers

from apps.todo.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'user', 'title', 'description',
                 'created_at', 'image')