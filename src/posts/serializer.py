from rest_framework import serializers
from django.utils.text import slugify
from .models import *


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title')


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('is_published', )


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'title')


class DetailVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Question
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['title'])

        return super().create(validated_data)

    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()
        extra_kwargs['slug'] = {'required': False}
        return extra_kwargs


class MentorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorCategory
        fields = ('id', 'name')


class MentorSerializer(serializers.ModelSerializer):
    category = MentorCategorySerializer(many=True, required=False)

    class Meta:
        model = Mentor
        fields = '__all__'
