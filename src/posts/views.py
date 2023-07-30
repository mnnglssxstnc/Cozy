from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from ..users.models import Profile
from .models import *
from .serializer import *


@api_view(['GET'])
def list_vacancy(request):
    vacancy = Vacancy.objects.filter(is_active=True)
    serializer = VacancySerializer(vacancy, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def detail_vacancy(request, vacancy_slug):
    try:
        vacancy = Vacancy.objects.get(slug=vacancy_slug)
    except Vacancy.DoesNotExist:
        return Response({'message': 'Vacancy not found'})

    serializer = DetailVacancySerializer(vacancy, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def company_list(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.filter(is_published=True)
    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def post_detail(request, post_url):
    try:
        post = Post.objects.get(slug=post_url)
    except Post.DoesNotExist:
        return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PostDetailSerializer(post, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def post_create(request):
    serializer = PostCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


@permission_classes([permissions.IsAuthenticated])
@api_view(['PUT'])
def update_post(request, post_url):
    try:
        post = Post.objects.get(slug=post_url)
    except Post.DoesNotExist:
        return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.user == post.user:
        serializer = PostCreateSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({'message': 'This is not your post'})


@permission_classes([permissions.IsAuthenticated])
@api_view(['DELETE'])
def post_delete(request, post_url):
    try:
        post = Post.objects.get(slug=post_url)
    except Post.DoesNotExist:
        return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.user == post.user:
        post.delete()
        return Response({'message': 'Delete'})

    return Response({'message': 'This is not your post'})


@api_view(['GET'])
def list_mentors(request):
    mentors = Mentor.objects.all()
    serializer = MentorSerializer(mentors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def create_mentor(request):
    profile = Profile.objects.get(user=request.user)
    if profile.is_mentor:
        mentor_data = request.data.copy()
        mentor_data['user'] = request.user.id

        serializer = MentorSerializer(data=mentor_data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({'message': 'You are not a mentor'})


@permission_classes([permissions.IsAuthenticated])
@api_view(['PUT'])
def update_mentor(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return Response({'message': 'Profile not found'}, status=status.HTTP_403_FORBIDDEN)

    if profile.is_mentor:
        try:
            mentor = Mentor.objects.get(user=request.user)
        except Mentor.DoesNotExist:
            return Response({'message': 'Mentor not found'})

        serializer = MentorSerializer(mentor, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'You are not a mentor'})


