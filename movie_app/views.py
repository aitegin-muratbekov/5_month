from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializers, MovieSerializers, ReviewSerializers
from .models import Director, Movie, Review
from rest_framework import status

@api_view(['GET'])
def director_view(request):
    directors = Director.objects.all()
    serializers = DirectorSerializers(directors, many=True)

    return Response(data=serializers.data)

@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'opana': 'NETU TAKOGO'}, status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializers(director).data
    return Response(data=data)

@api_view(['GET'])
def movie_view(request):
    movies = Movie.objects.all()
    serializers = MovieSerializers(movies, many=True)

    return Response(data=serializers.data)

@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'opana': 'NETU TAKOGO'}, status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializers(movie).data
    return Response(data=data)
@api_view(['GET'])
def review_view(request):
    reviews = Review.objects.all()
    serializers = ReviewSerializers(reviews, many=True)

    return Response(data=serializers.data)

@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'opana': 'NETU TAKOGO'}, status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializers(review).data
    return Response(data=data)