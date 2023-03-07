from rest_framework import serializers
from .models import Articles


class ArticlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('title','main_text')