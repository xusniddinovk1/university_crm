from rest_framework import serializers
from ..models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment  # Model nomi
        fields = ['id', 'student', 'amount', 'date', 'status']
