from datetime import datetime
from django.contrib.auth.password_validation import validate_password, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import get_routes


class Access(APIView):
    def get(self, request):
        user = self.request.user

        return Response({
            "id": user.id,
            "is_active": user.is_active,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "is_superuser": user.is_superuser,
            "first_login": not user.last_login,
            "routes": get_routes(self.request.user),
        })


class NewPassword(APIView):
    def post(self, request):
        try:
            validate_password(request.data["password"], request.user)
        except ValidationError as errors:
            return Response({ "errors": errors, "success": False })

        request.user.set_password(request.data["password"])
        request.user.last_login = datetime.now()
        request.user.save()

        return Response({ "success": True })


class ChangePassword(APIView):
    def post(self, request):
        if not request.user.check_password(request.data["current"]):
            return Response({ "success": False, "errors": ["Senha atual inválida."] })

        try:
            validate_password(request.data["password"], request.user)
        except ValidationError as errors:
            return Response({ "errors": errors, "success": False })

        request.user.set_password(request.data["password"])
        request.user.last_login = datetime.now()
        request.user.save()

        return Response({ "success": True })
