from rest_framework import serializers
from app.models import Question, Poll, Option

class QuestionCreate(serializers.Serializer):
    question = serializers.CharField()
    option1 = serializers.CharField()
    option2 = serializers.CharField()
    option3 = serializers.CharField()
    option4 = serializers.CharField()
    
    def create(self, validated_data):
        q = Question.objects.create(name=validated_data.get("question"))
        q.options.create(name=validated_data.get("option1"))
        q.options.create(name=validated_data.get("option2"))
        q.options.create(name=validated_data.get("option3"))
        q.options.create(name=validated_data.get("option4"))
        p = Poll.objects.get(question=q)
        return p

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance
    
    
class Question(serializers.ModelField):
    ...