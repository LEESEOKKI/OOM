# 회원가입, 로그인, 로그아웃

### 1. accounts 앱 생성

    AbstractUser 함수 활용.

### 2. CORS header 라이브러리 준비

    CORS는 추가 HTTP Header를 사용해 다른 출처의 자원에 접근케 하는 권한 부여.
    $ pip install django-cors-headers
    
    $ pip freeze > requirements.txt
    
    INSTALLED_APPS = [
    
    'corsheaders',
    ]
    
    
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
    ]
    
    CORS_ALLOWED_ORIGINS = [
        'http://localhost:8080',
    ]
    
    # 이 origin만 선택적으로 허용하겠다.

### 3. dj_rest_auth 패키지를 이용해 인증(ex 회원가입, 로그인...)

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movies.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    ]
    dj_rest_auth 패키지 사용하기 위해 위와 같은 경로 설정.
    
    $ pip install dj-rest-auth
    
    INSTALLED_APPS = [
    
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    
    ]
    이렇게 설정한 후 http://127.0.0.1:8000/accounts/ url로 들어가보면 자동으로 회원가입, 로그인, 로그아웃 등의 새로운 url 경로가 생긴 것이 보임.
    
    회원가입 기능을 이용하기 위해 django-allauth 필요
    
    $ pip install 'dj-rest-auth[with_social]'
    
    INSTALLED_APPS = [
    
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    
    ]
    
    SITE_ID = 1
    
    REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    }
    # 우리는 비밀번호 변경하지 않지만 비밀번호 변경하기 위해선 위의 코드 필요.
    
    REST_FRAMEWORK = {
    
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ],
    }
    # 접근 허가를 모두로 설정하기 위해 위의 코드 사용. 후에 permission 데코레이터를 이용해 특정 기능에는 인증된 사용자만 이용하게끔 가능.

# Home, 디테일, 추천 페이지에 필요한 모델 생성

## BackEnd

### 1. movies앱 모델

    class Genre
    - genre_ids 번호에 맞는 장르 name 보유.
    
    class Tmdb
    - tmdb api에서 받아온 추천 영화 리스트 보유.
    - Genre와 genre_ids를 통해 M:N 관계
    
    class Kobis
    - kobis api에서 현재 상영작 받아온 정보 보유.
    
    class Detail
    - kobis api에 없는 포스터 사진 경로와 영화 분류 데이터 크롤링 해온 정보.

### 2. movie앱 serializer

    MovieListSerializer
    - tmdb 영화 모든 필드.
    
    MovieIdSerializer
    - Genre와 참조하기 위한 Tmdb 모델의 serializer.
    - tmdb 필드 중 title, poster_path, overview.
    
    GenreListSerializer
    - MovieIdSerializer 데이터 역참조.
    - 추천 알고리즘 영화 선정에 필요.
    
    GenreDetailSerializer
    - 바로 위에 serializer와 동일 
    - viwe함수 수정하고 serializer 삭제 필요.
    
    MovieDetailSerializer
    - genre_ids는 참조해줄 필요가 없었는데 생성
    - viwe함수 수정하고 serializer 삭제 필요.
    
    MovieNowSerializer
    - Kobis 모델에 해당하는 poster_url과 영화 분류 데이터.
    - 메인 페이지이자 현재 상영작 리스트에 사용.
    
    KobisSerializer
    - Kobis api에서 받아온 데이터
    - 현재 상영작 리스트의 디테일에 사용.

### 3. movie앱 url 및 views

    1. path('genres/', views.genre_list)
    1-1. @api_view(['GET'])
         def genre_list(request):
             genres = Genre.objects.all()
             serializer = GenreListSerializer(genres, many=True)
             return Response(serializer.data)
    1-2. 장르별 영화 데이터 리스트.
    
    2. path('genres/<int:genre_pk>/', views.genre_detail)
    2-2. @api_view(['GET'])
        def genre_detail(request, genre_pk):
            genre = Genre.objects.get(pk=genre_pk)
            serializer = GenreDetailSerializer(genre)
            return Response(serializer.data)
    2-3. 특정 장르의 영화 데이터 모음.
    
    3. path('movielist/', views.movielist)
    3-1. @api_view(['GET', 'POST'])
        def movielist(request):
            if request.method == 'GET':
                movies = get_list_or_404(Tmdb)
                serializer = MovieListSerializer(movies, many=True)
                return Response(serializer.data)
    3-2. vue.js의 state.movies에 데이터 저장하기 위한 url.
    
    4. path('kobislist/', views.kobislist)
    4.1 @api_view(['GET', 'POST'])
        def kobislist(request):
            if request.method == 'GET':
                kobises = get_list_or_404(Kobis)
                serializer = KobisSerializer(kobises, many=True)
                return Response(serializer.data)
    4.2 kobis api 추천 영화에 쓰일 데이터.
    
    5. path('nowlist/', views.nowlist)
    5.1 @api_view(['GET', 'POST'])
        def nowlist(request):
            if request.method == 'GET':
                details = get_list_or_404(Detail)
                serializer = MovieNowSerializer(details, many=True)
                return Response(serializer.data)
    5.2 kobis 영화에 쓰이는 poster_url 데이터.
    
    6. path('movielist/<int:tmdb_id>', views.movie_detail)
    6.1 @api_view(['GET'])
        def movie_detail(request, tmdb_id):
            movie = get_object_or_404(Tmdb, id=tmdb_id)
            serializer = MovieDetailSerializer(movie)
            return Response(serializer.data)
    6.2 추천 영화 id별 데이터.
    
    7. path('nowlist/<int:detail_id>', views.now_detail)
    7.1 @api_view(['GET'])
        def now_detail(request, detail_id):
            detail = get_object_or_404(Detail, id=detail_id)
            serializer = MovieNowSerializer(detail)
            return Response(serializer.data)
    7.2 현재 상영작 개별 데이터.

## FrontEnd

### 1. 컴포넌트 구성

    [App.vue]
    현재 상영 리스트를 보여주는 Homeview 라우터.
    게시글과 관련된 CommunityView 라우터.
    장르별 추천 영화 보여주는 RecommendView 라우터.
    회원가입, 로그인, 로그아웃 SignUp, Login라우터.
    
    [SignUpView]
    username과 password1, password2를 signUp 메소드를 사용해 data에 저장.
    store에 signUp으로 post로 axios 요청.
    
    [LogInView]
    username과 password를 logIn 메소드를 사용해 data에 받아오기.
    store에 logIn으로 post로 axios 요청.
    회원가입과 로그인이 성공하면 SAVE_TOKEN으로 토큰을 저장하고
    home으로 바로 이동하게끔 router.push
    
    [HomeView]
    created에 현재 상영작 데이터인 Detail과 Kobis를 요청하는 함수를
    실행하는 getDetails와 getKobises
    computed의 islog를 통해 현재 토큰이 True인지 False인지에 따라 
    로그인 버튼 또는 로그아웃 버튼이 보이게끔 설정.
    로그아웃은 store에서 버튼을 누르면 Token이 False가 되도록 설정.
    이 방식은 DB에서 완전히 제거할 수 있는 방식이 아니라 추후 수정이 필요해 보임.
    현재 상영작 리스트인 NowMovie 컴포넌트 import.
    
    [NowMovie]
    computed에 store에 저장된 details 가져오기.
    NowMovieItem 컴포넌트를 import
    v-for문 이용하여 details를 하나씩 detail이라는 데이터로 자식
    컴포넌트와 연결
    
    [NowMovieItem]
    props로 detail 데이터 받아오기.
    computed에 앞서 store에 저장된 kobises 데이터 가져오기.
    kobises 데이터를 v-for문을 이용해 하나의 개별 데이터로 분류.
    v-if 조건문 사용하여 detail.id와 kobis.id가 같을 경우 
    detail에는 없고 kobis에 있는 영화 제목 나타내기.
    영화 제목과 함께 순위 상승 숫자도 함께 저장되어 있어서
    split을 사용하여 영화 제목만 추출.
    마찬가지로 detail에 영화 분류 데이터들이 '|' 문자와 연결되어 있어
    split 사용하여 각자 데이터로 추출.
    
    [RecommendView]
    created에 Tmdb 영화 데이터와 장르 데이터를 store에 저장시키는 
    액션을 요청하는 메소드 실행.
    MovieList 컴포넌트를 import.
    
    [MovieList]
    computed에 앞서 store에 저장된 장르 데이터 가져오기.
    MovieListItem 컴포넌트를 import
    v-for문을 이용해 genres를 하나씩 genre라는 데이터로 자식 
    컴포넌트와 연결.
    
    [MovieListItem]
    props로 genre 데이터 받아오기.
    vue-flashcard 컴포넌트를 import하여 플립 카드 형태 사용.

### 2. 추천 알고리즘**

    2-1. 랜덤으로 몇개의 영화를 제시하여 사용자가 선호하는 영화와
         선호하지 않는 영화 데이터를 저장하여 추천 알고리즘을 작성하려고 함.
    
         하지만 사용자 인증 활용에 익숙지 않아 MovieList에 모든 장르를 보여주고
         flashcard를 이용해 클릭하면 뒷면에 각 장르마다 추천 영화가
         랜덤으로 1개씩 나오도록 알고리즘 작성.
    
    2-2. 카드 뒷면에 랜덤 영화의 제목과 포스터를 한 번에 보여주기 위해
         genre.tmdbs[Math.floor(Math.random() * this.genre.tmdbs.length)].title
         genre.tmdbs[Math.floor(Math.random() * this.genre.tmdbs.length)].poster_path
         이러한 방식으로 바로 template에 작성.
    
         하지만 이렇게 되면 랜덤 함수가 두 번 실행되어서 영화 제목과
         포스터가 다르게 나옴.
         그리하여 data에 randomitem이라는 이름으로 한 번만 랜덤이
         실행되도록 설정.
