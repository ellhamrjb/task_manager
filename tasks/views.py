from django.shortcuts import render
from rest_framework import viewsets
from .models import Project, Task, Comment, Tag, Attachment
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer, TagSerializer, AttachmentSerializer


def home(request):
    return render(request, 'tasks/home.html')

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer