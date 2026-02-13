from rest_framework import serializers     
#serializers.py переводит данные с sql формата (базы) на удобный формат для чтения для фронтенд 
#разработчика (JSON формат)
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id',
            'title',
            'body',
        )