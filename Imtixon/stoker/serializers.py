from rest_framework import serializers
from .models import Comments, Clients, Services, Advisers, FAQs, Features


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('slug', 'title', 'description', 'image', 'price')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('first_name', 'last_name', 'email', 'phone', 'image', 'username')


class CommentsSerializer(serializers.ModelSerializer):
    services = ServiceSerializer()
    clients = ClientSerializer()

    class Meta:
        model = Comments
        fields = ('comment', 'clients', 'services')


class AdvisersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisers
        fields = ('first_name', 'last_name', 'slug', 'email', 'image', 'level')


class FAQsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQs
        fields = ('question', 'answer')


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ('title', 'image', 'description')
