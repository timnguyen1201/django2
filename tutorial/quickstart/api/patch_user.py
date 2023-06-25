from rest_framework import generics, serializers,permissions
from rest_framework.response import Response


class MePatchUser(serializers.Serializer):
    email = serializers.CharField()
    username = serializers.CharField()


class MePatchApi(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch_data(self, request):
        serializer = self.patch(request.user)
        return Response(serializer.data)