from rest_framework import serializers
from .models import Course, Chapter, Assignment, UserProfile

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'type', 'password')

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['assignment_id', 'order', 'course_id', 'chapter_id', 'title', 'description']

class ChapterSerializer(serializers.ModelSerializer):
    chapter_assignment = AssignmentSerializer(many=True, read_only=True)
    class Meta:
        model = Chapter
        fields = ['chapter_id', 'order', 'course_id', 'chapter_name', 'created', 'modified', 'chapter_assignment']


class CourseSerializer(serializers.ModelSerializer):
    course_chapter = ChapterSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['course_id', 'order', 'course_name', 'description', 'created', 'modified', 'course_chapter']
