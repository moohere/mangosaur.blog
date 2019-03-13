from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime
from vote.models import VoteModel

class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table =  'user'

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'category'
  
    def __str__(self):
        return self.name

class Post(VoteModel, models.Model):
    title = models.CharField(max_length=150,  unique=True)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    thumbnail = models.ImageField(upload_to="thumbnail/", blank=True)
    date_created = models.DateTimeField(default=datetime.now)
    date_edited = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'post'
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def recent(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=1)

    recent.admin_order_field = 'date_created'
    recent.boolean = True
    recent.short_description = "Recent?"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    date_created = models.DateTimeField(default=datetime.utcnow)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment'
        ordering = ['-date_created']