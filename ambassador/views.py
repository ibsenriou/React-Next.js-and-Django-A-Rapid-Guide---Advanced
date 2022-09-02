from rest_framework.response import Response
from rest_framework.views import APIView

from ambassador.serializers import ProductSerializer
from core.models import Product


class ProductFrontendAPIView(APIView):
    def get(self, _):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductBackendAPIView(APIView):
    def get(self, _):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
