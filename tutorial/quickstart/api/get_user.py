from rest_framework import generics, mixins, views, serializers, permissions
from rest_framework.response import Response


class MeSerializer(serializers.Serializer):
    email = serializers.CharField()
    #etc


class MeApi(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MeSerializer

    def get(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
