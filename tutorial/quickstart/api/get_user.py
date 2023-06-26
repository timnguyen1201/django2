from rest_framework import generics, serializers, permissions
from rest_framework.response import Response


class MeSerializer(serializers.Serializer):
    email = serializers.CharField()
    username = serializers.CharField()


class MeApi(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MeSerializer

    def get(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
