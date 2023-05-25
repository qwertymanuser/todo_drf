from rest_framework import serializers

from apps.users.models import User
from apps.todo.serializers import ToDoSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'age', 'phone_number')
        
class UserDetailSerializer(serializers.ModelSerializer):
    users_todo = ToDoSerializer(many=True, read_only=True)
    class Meta:
        model = User 
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'age', 'phone_number', 'users_todo')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=100, write_only=True
    )
    password2 = serializers.CharField(
        max_length=100, write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'age', 'phone_number', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password' : 'Пароли отличаются'})
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError({'phone_number' : 'Напишите номер с +996'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            age=validated_data['age'],
            phone_number=validated_data['phone_number'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user