import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

TEACHER = 'TE'
STUDENT = 'ST'
UNKNOWN = 'UN'
TYPE_CHOICES = (
(TEACHER, 'Teacher'),
(STUDENT, 'Student'),
(UNKNOWN, 'Unknown'),
)

# Create your models here.

class UserProfile(AbstractUser):
    type = models.CharField(choices=TYPE_CHOICES, max_length=20, default=UNKNOWN)

    def __str__(self):
        return self.username

class Course(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course_name = models.CharField(max_length=1000)
    description = models.CharField(blank=True, null=True, max_length=5000)
    order = models.IntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name

class Chapter(models.Model):
    chapter_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course_id = models.ForeignKey('Course', related_name='course_chapter', on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=256, null=False, blank=False)
    order = models.IntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chapter_name

class Assignment(models.Model):
    assignment_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    order = models.IntegerField(default=0, blank=False, null=False)
    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(blank=True, null=True, max_length=5000)
    course_id = models.ForeignKey('Course', related_name='course_assignment', on_delete=models.CASCADE)
    chapter_id = models.ForeignKey('Chapter', related_name='chapter_assignment', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)