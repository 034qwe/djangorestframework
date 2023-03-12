from rest_framework import serializers
from .models import Articles


class ArticlesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    anons =serializers.CharField()
    main_text =serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    categ_id = serializers.IntegerField()


    def create(self, validated_data):
        return Articles.objects.create(**validated_data) 
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.anons = validated_data.get('anons',instance.anons)
        instance.main_text = validated_data.get('main_text',instance.main_text)
        instance.updated_at = validated_data.get('updated_at',instance.updated_at)
        instance.categ_id = validated_data.get('categ_id',instance.categ_id)

        instance.save()

        return instance