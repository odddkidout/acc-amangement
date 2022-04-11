from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import AccSerializer
from .models import Acc, LockedAcc
from rest_framework import viewsets

class accviewset(viewsets.ModelViewSet):
    queryset = Acc.objects.all()
    serializer_class = AccSerializer
    def create(self, request, *args, **kwargs):
        serializer = AccSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class lockedaccviewset(viewsets.ModelViewSet):
    queryset = LockedAcc.objects.all()
    serializer_class = AccSerializer

    def create(self, request, *args, **kwargs):
        serializer = AccSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)