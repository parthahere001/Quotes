from rest_framework import serializers
from .models import QuoteModel

class QuoteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = False)

    class Meta:
        model = QuoteModel
        fields = ['id', 'name', 'details']
        extra_kwargs = {'name' : { 'read_only' : False }}