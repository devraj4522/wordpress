from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (('draft', "Draft"), ('published', 'Published'))

    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=60, unique_for_date='publish', )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    heading = models.CharField(max_length=60, default='')
    image = models.ImageField(default='', blank=True, upload_to="blog/images/%Y/%m/%d/")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='draft')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manage
    
    # SEO Columns
    meta = models.TextField(default='')
    desc = models.TextField(default='')

    def __str__(self):
        return "Post By - {} - on - {}".format(self.author, self.title)

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "{} - Commented on -{}".format(self.name, self.post)

class PostSubscriber(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Email by - {self.email} on {self.title}"

    class Meta:
        ordering = ('-created',)
