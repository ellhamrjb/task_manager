from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number=models.CharField(max_length=20,blank=True)
    
class Project(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()
    
    def __str__(self):
        return self.name

class Task(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    due_at=models.DateTimeField()
    completed_at=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    tasks = models.ManyToManyField(Task, related_name='tags')

    def __str__(self):
        return self.name
    
class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    