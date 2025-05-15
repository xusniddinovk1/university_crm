from rest_framework import serializers  # DRF serializerlarini yaratish uchun modul
from ..models import *  # Serializer uchun kerak bo'lgan modullar
# GroupStudent modeli uchun serializer
from rest_framework import serializers


# Day modeli uchun serializer
class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day  # Model nomi
        fields = ['id', 'title', 'descriptions']  # Seriyalizatsiya qilinadigan maydonlar


class GroupStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = ['id', 'title', 'course', 'teacher', 'start_date', 'end_date', 'descriptions']
