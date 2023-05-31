from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('genres/', views.genre_list),
    path('genres/<int:genre_pk>/', views.genre_detail),
    path('movielist/', views.movielist),
    path('kobislist/', views.kobislist),
    path('nowlist/', views.nowlist),
    path('movielist/<int:tmdb_id>', views.movie_detail),
    path('nowlist/<int:detail_id>', views.now_detail),

        # comment
    path('nowlist/<int:detail_id>/comments/', views.comment_create),
    path('<int:detail_id>/comments/', views.get_comment_list),
    path('comments/<int:comment_id>/', views.comment_delete),
]