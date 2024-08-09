from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from main.models import *


class Xodimlar_nameSerializer(ModelSerializer):
    class Meta:
        model = Xodimlar_name
        fields = '__all__'

class AttendanceSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        