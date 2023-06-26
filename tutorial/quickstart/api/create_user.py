from rest_framework import generics, serializers, permissions
from rest_framework.response import Response


class MeCreateUser(serializers.Serializer):
    email = serializers.CharField()
    username = serializers.CharField()


class MeCreateApi(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def create_data(self, request):
        serializer = self.post(request.user)
        return Response(serializer.data)
