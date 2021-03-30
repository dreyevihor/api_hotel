from rest_framework import serializers
from hotel_admin.models import News


class NewsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
            max_length=None, use_url=True
        )

    class Meta:
        model = News
        fields = ("id", "title", "text", "image")
