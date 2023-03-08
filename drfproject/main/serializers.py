from rest_framework import serializers
from .models import Articles


class ArticlesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    anons =serializers.CharField()
    main_text =serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    categ_id = serializers.IntegerField()
