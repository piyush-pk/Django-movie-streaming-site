from django.db import models



# Create your models here.
class Category(models.Model):
    Category = models.CharField(max_length=255)

    def __str__(self):
        return self.Category


class Movies(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.FloatField()
    link = models.URLField()
    slug = models.SlugField(max_length=255, null = True, blank =True)
    desc = models.TextField()
    thumbnail = models.ImageField(upload_to = 'static/thumbnail/')
    images = models.ImageField(upload_to = 'static/img/')
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name