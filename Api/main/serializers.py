from dataclasses import fields
from rest_framework import serializers
from .models import Acc

class AccSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acc
        fields = "__all__"