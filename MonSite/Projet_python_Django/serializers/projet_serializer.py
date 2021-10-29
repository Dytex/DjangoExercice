from rest_framework import serializers
from Projet_python_Django.models import Projet


class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = serializers.ALL_FIELDS
