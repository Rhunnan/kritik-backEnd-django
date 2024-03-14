from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('name', 'reviews', 'bookmarks')


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Establishment
        fileds = ('path_image','name','location','category','description','address','ai_script','reviews')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ('name','review_comment','star_rating','image_path','establishment_name')