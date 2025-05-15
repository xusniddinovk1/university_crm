from ..models import *
from rest_framework import serializers


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day  # Model nomi
        fields = ['id', 'title', 'descriptions']


class GroupStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = ['id', 'descriptions', 'title', 'course', 'teacher', 'start_date', 'end_date']
