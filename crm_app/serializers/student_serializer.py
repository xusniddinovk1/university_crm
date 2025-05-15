from .user_serializer import *
from ..models import Student, Parents


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        groups = validated_data.pop('group', [])

        user = UserSerializer().create(user_data)
        student = Student.objects.create(user=user, **validated_data)

        student.group.set(groups)  # (add groups bt set() function)
        return student

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)

        if user_data:
            UserSerializer().update(instance.user, user_data)

        for attr, value in validated_data.items():
            field = instance._meta.get_field(attr)
            if field.many_to_many:
                getattr(instance, attr).set(value)
            else:
                setattr(instance, attr, value)

        instance.save()
        return instance


class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = ['id', 'descriptions', 'student', 'full_name', 'phone_number', 'address']
