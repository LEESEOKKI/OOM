from rest_framework import serializers
from .models import Genre,Tmdb, Detail, Kobis, Comment



class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tmdb
        fields = '__all__'

class MovieIdSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tmdb
        fields = ('title','poster_path','overview',)

class GenreListSerializer(serializers.ModelSerializer):
    tmdbs = MovieIdSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'

class GenreDetailSerializer(serializers.ModelSerializer):
    tmdbs = MovieIdSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'
        
class MovieDetailSerializer(serializers.ModelSerializer):
    genre_ids = GenreListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Tmdb
        fields = '__all__'

class KobisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kobis
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)
  
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('detail',)
        
class MovieNowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Detail
        fields = '__all__'