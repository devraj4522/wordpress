from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Category(models.Model):
    CLASS_CHOICES = (('matric', 'Matric'), ('inter', "Inter"), ('graduation', 'Graduation'),
                     ('post_graduation', 'Post-Graduation'))
    class_category = models.CharField(max_length=25, choices=CLASS_CHOICES,
                                      default='inter')
    post_category = models.CharField(max_length=50)

    def __str__(self):
        return "For Class {} in the field of {}".format(self.class_category,
                                                        self.post_category)


class SubCategory(models.Model):
    POST_CHOICES = (('admit_card', 'Admit Card'), ('result', 'Result')
                    , ('entries', "Entries"))
    choice = models.CharField(choices=POST_CHOICES, max_length=20)

    def __str__(self):
        return f'{self.choice}'


class Post(models.Model):
    STATUS_CHOICES = (('draft', "Draft"), ('published', 'Published'))

    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='category', default='')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE,
                                     related_name='sub_category', default='')
    slug = models.SlugField(max_length=60, unique_for_date='publish',)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='openings_post')
    image = models.ImageField(default='', blank=True, upload_to='job_openings/images')
    desc = models.TextField(default='')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='draft')

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manage

    def get_absolute_url(self):
        return reverse('job_openings:postView', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=70)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "{} - Commented on -{}".format(self.name, self.post)


class Link(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ManyToManyField(Post, blank=True, related_name='links')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('-created',)


class Email(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=60, default='')

    def __str__(self):
        return f"Email by - {self.email} on {self.post_title}"

    class Meta:
        ordering = ('-created',)