from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import PasswordResetSerializer, PasswordResetValidationSerializer


class PasswordResetView(GenericAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('email')
        serializer.send_password_reset_email(user.email, user.profile.registration_code)
        return Response(f'Password reset sent to email {user.email}!')


class PasswordResetValidationView(GenericAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = PasswordResetValidationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer.validated_data)
        return Response(f'New password was set!')
