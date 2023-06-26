from rest_framework import generics, serializers, permissions
from rest_framework.response import Response


class MeSerializer(serializers.Serializer):
    email = serializers.CharField()
    username = serializers.CharField()


class MeApi(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MeSerializer

    def delete_data(self, request):
        serializer = self.delete(request.user)
        return Response(serializer.data)
