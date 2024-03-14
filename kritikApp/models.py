from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    review_comment = models.TextField(blank=True, default='')
    star_rating = models.FloatField(default=0)
    image_path = models.CharField(max_length=255, blank=True, default='')
    establishment_name = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.name

class Establishment(models.Model):
    path_image = models.CharField(max_length=255, blank=True, default='')
    name = models.CharField(max_length=255, blank=True, default='')
    location = models.CharField(max_length=255, blank=True, default='')
    category = models.CharField(max_length=255, blank=True, default='')
    description = models.CharField(max_length = 255, blank=True, default='')
    address = models.CharField(max_length=255, blank=True, default='')
    ai_script = models.CharField(max_length=255,blank=True, default='')
    reviews = models.ManyToManyField(Review, blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    reviews = models.ManyToManyField(Review, blank=True)
    bookmarks = models.ManyToManyField(Establishment, blank=True)

    def __str__(self):
        return self.name
