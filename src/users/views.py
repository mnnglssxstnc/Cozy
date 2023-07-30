from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from .models import CustomUser, Profile
from .serializer import RegisterUserSerializer, AuthUserSerializer, ProfileSerializer


class UserRegister(generics.GenericAPIView):
    """Реєстрація користувача"""

    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AuthUser(ObtainAuthToken):
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(password):
            return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class UserLogout(generics.DestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(user=request.user)
        except Token.DoesNotExist:
            return Response({'message': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        token.delete()

        return Response({'message': 'Delete'})


@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def user_profile(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)


@permission_classes([permissions.IsAuthenticated])
@api_view(['PUT'])
def profile_update(request):
    if request.method == 'PUT':
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = ProfileSerializer(profile, data=request.data)

            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Profile.DoesNotExist:
            return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)


# @permission_classes([permissions.IsAuthenticated])
# @api_view(['GET', 'POST', 'PUT'])
# def user_profile(request):
#     if request.method == 'GET':
#         try:
#             profile = Profile.objects.get(user=request.user)
#             serializer = ProfileSerializer(profile)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Profile.DoesNotExist:
#             return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'POST':
#         try:
#             profile = Profile.objects.get(user=request.user)
#         except Profile.DoesNotExist:
#             serializer = ProfileSerializer(data=request.data)
#
#             if serializer.is_valid():
#                 serializer.save(user=request.user)
#
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)


# class UserProfile(generics.GenericAPIView):
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
#     def post(self, request):
#         try:
#             profile = Profile.objects.get(user=request.user)
#         except Profile.DoesNotExist:
#             profile = Profile.objects.create(user=request.user)
#
#         serializer = self.serializer_class(profile, many=False)
#
#         serializer.is_valid(raise_exception=True)
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data, status=status.HTTP_200_OK)
#         #
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request):
#         try:
#             profile = Profile.objects.get(user=request.user)
#         except Profile.DoesNotExist:
#             profile = Profile.objects.create(user=request.data)
#
#         serializer = self.serializer_class(profile, instance=profile, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

