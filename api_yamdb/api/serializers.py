from datetime import datetime
import re

from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.db.models import Avg

from reviews.models import (
    Category, Comment, Genre, Review, Title
)
from users.models import User


class CategorySerializer(serializers.ModelSerializer):

    def validate_slug(self, value):
        if not re.match('^[-a-zA-Z0-9_]+$', value):
            raise serializers.ValidationError('Некоректный slug')
        return value
    
    class Meta:
        model = Category
        fields = ('name', 'slug')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')

    def validate_slug(self, value):
        if not re.match('^[-a-zA-Z0-9_]+$', value):
            raise exceptions.ValidationError('Некоректный slug')
        return value


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    def validate_score(self, value):
        """Check that score in range 0 - 10"""
        if value > 10 or value < 0:
            raise serializers.ValidationError("Score not in range 0-10")
        return value

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        many=True, queryset=Genre.objects.all(), slug_field='slug'
    )
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        rating = obj.reviews.aggregate(Avg('score'))['score__avg']
        if rating is not None:
            return round(rating)
        return None

    class Meta:
        model = Title
        fields = ['id', 'name', 'year', 'rating',
                  'description', 'genre', 'category']
        read_only_fields = ['id']

    def validate_year(self, value):
        year_now = datetime.now().year
        if value > year_now:
            raise serializers.ValidationError(
                "Будущее еще не наступило")
        return value

    def create(self, validated_data):
        genre_data = validated_data.get('genre')
        category_data = validated_data.get('category')
        if category_data is not None:
            category = get_object_or_404(Category, slug=category_data)
            validated_data['category'] = category
        instance = super().create(validated_data)
        if genre_data is not None:
            for slug in genre_data:
                genre = get_object_or_404(Genre, slug=slug)
                instance.genre.add(genre)
        instance.save()
        return instance

    def to_representation(self, instance):
        self.fields['category'] = CategorySerializer()
        return super().to_representation(instance)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'bio', 'role']
