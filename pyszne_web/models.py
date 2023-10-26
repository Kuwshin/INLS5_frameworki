from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, blank=False, unique=False)
    year = models.PositiveSmallIntegerField(default=2023)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title_with_year()
    def title_with_year(self):
        return f"{self.title} ({self.year})"
   
