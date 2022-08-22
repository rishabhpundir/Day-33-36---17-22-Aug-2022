from django.urls import path, include
from apiapp import views

urlpatterns = [
    path('courses/', views.CourseView.as_view()),
    path('courses/<pk>/', views.CourseEditView.as_view()),
    path('chapters/', views.ChapterView.as_view()),
    path('chapters/<pk>/', views.ChapterEditView.as_view()),
    path('assignments/', views.AssignmentView.as_view()),
    path('assignments/<pk>/', views.AssignmentEditView.as_view()),
    path('register/', views.RegisterView.as_view()),
    # path('login/', views.LoginAPI.as_view(), name='login'),
    # path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
