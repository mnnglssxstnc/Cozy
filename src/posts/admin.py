from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', )

    prepopulated_fields = {'slug': ('title', )}


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(MentorCategory)
class MentorCategoryAdmin(admin.ModelAdmin):
    list_display = ('id',)

