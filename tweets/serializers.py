from rest_framework import serializers
from .models import Tweet

MAX_LENGTH = 240

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content']

    def validate_content(self, value):
        if len(value) > MAX_LENGTH:
            raise serializers.ValidationError("This tweet is too long")
        return value
