from rest_framework import serializers
from .models import Rate

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'
# class HistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = History
#         fields = '__all__'