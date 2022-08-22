from django.contrib import admin
from .models import Course, Chapter, Assignment, UserProfile
from .forms import CustomUserProfileForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = UserProfile
    add_form = CustomUserProfileForm
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'type', 'is_staff', 'is_superuser')

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User type',
            {
                'fields':('type',)
            }
        )
    )


admin.site.register(UserProfile, CustomUserAdmin)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'order', 'course_name', 'description', 'created', 'modified', 'course_chapter']

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['chapter_id', 'order', 'course_id', 'chapter_name', 'created', 'modified', 'chapter_assignment']

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['assignment_id', 'order', 'course_id', 'chapter_id', 'title', 'description']