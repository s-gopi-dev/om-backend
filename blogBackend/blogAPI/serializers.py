from rest_framework import serializers
from .models import User, Blog
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class BlogSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'
    
    def get_author(self, obj):
        return obj.author.username
    
    def validate_title(self, value):
        if '<script>' in value.lower():
            raise serializers.ValidationError("Invalid content in title")
        return value

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims if needed
        token['email'] = user.email
        token['username'] = user.username
        return token

    def validate(self, attrs):
        # change to use email instead of username
        attrs['username'] = attrs.get('email')
        response = super().validate(attrs)

        response['username'] = self.user.username
        return response