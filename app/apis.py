# Standard Library
import json

# Third Party Packages
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from app.serializers import UserLoginSerializer
from app.utils import get_field_errors


@api_view(('POST',))
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.get(username=request.data.get('username'))
        if not Token.objects.filter(user=user).exists():
            token = Token.objects.create(user=user)
        else:
            Token.objects.get(user=user).delete()
            token = Token.objects.create(user=user)
        return Response({
            'status': status.HTTP_200_OK,
            'access_token': token.key,
            'user_id': user.id
        }, status=status.HTTP_200_OK)

    else:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'errors': get_field_errors(serializer.errors),
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def user_logout(request):
    Token.objects.get(user=request.user).delete()
    return Response({'message': 'Logout Successful!'}, status=status.HTTP_200_OK)



