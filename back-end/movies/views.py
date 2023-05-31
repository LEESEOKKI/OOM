from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import GenreListSerializer, MovieListSerializer, MovieIdSerializer, GenreDetailSerializer, MovieDetailSerializer, KobisSerializer, MovieNowSerializer, CommentSerializer

from .models import Genre, Tmdb, Kobis, Detail, Comment


# Create your views here.
@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre = Genre.objects.get(pk=genre_pk)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def movielist(request):
    if request.method == 'GET':
        movies = get_list_or_404(Tmdb)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, tmdb_id):
    movie = get_object_or_404(Tmdb, id=tmdb_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)
    

@api_view(['GET', 'POST'])
def kobislist(request):
    if request.method == 'GET':
        kobises = get_list_or_404(Kobis)
        serializer = KobisSerializer(kobises, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def nowlist(request):
    if request.method == 'GET':
        details = get_list_or_404(Detail)
        serializer = MovieNowSerializer(details, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def now_detail(request, detail_id):
    detail = get_object_or_404(Detail, id=detail_id)
    serializer = MovieNowSerializer(detail)
    return Response(serializer.data)

# comment
@api_view(['GET'])
def get_comment_list(request, detail_id):
    comments = Comment.objects.filter(detail=detail_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, detail_id):
    detail = get_object_or_404(Detail, id=detail_id)
    serializer = CommentSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(detail=detail)    
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

