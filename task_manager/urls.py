from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from tasks import views

router=DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'attachments', views.AttachmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('',include('tasks.urls')),
]
