from rest_framework import serializers
from .models import Tweet

MAX_LENGTH = 240
TWEET_ACTION_OPTIONS = ["like", 'unlike', 'retweet']

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content']

    def validate_content(self, value):
        if len(value) > MAX_LENGTH:
            raise serializers.ValidationError("This tweet is too long")
        return value


class TweetActionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action")
        return value
