from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializers(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movies_count(self, director):
        return director.movies_count()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class MovieSerializers(serializers.ModelSerializer):
    average = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = 'id title description duration director average'.split()
    def get_average(self, movie):
        return movie.average()

class MovieWithReviewSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True)
    class Meta:
        model = Movie
        fields = 'id title description duration director reviews'.split()
