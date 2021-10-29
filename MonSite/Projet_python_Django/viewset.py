from rest_framework import viewsets
from Projet_python_Django.models import Projet
from Projet_python_Django.serializers.projet_serializer import ProjetSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class ProjetViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Projet.objects.all()
        serializer = ProjetSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
