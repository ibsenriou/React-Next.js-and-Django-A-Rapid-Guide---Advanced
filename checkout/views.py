from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LinkSerializer
from core.models import Link


class LinkAPIView(APIView):

    def get(self, _, code=''):
        link = Link.objects.filter(code=code).first()
        serializer = LinkSerializer(link)
        return Response(serializer.data)
