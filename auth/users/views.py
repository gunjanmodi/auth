from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .producer import publish
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        products = User.objects.all()
        serializer = UserSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = User.objects.get(id=pk)
        serializer = UserSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = User.objects.get(id=pk)
        serializer = UserSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = User.objects.get(id=pk)
        product.delete()
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
