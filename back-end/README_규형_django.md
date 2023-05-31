# final_pjt

## DIM.

| API 가져오기                                     |
| -------------------------------------------- |
| 로그인                                          |
| 회원가입                                         |
| 영화 추천(알고리즘)                                  |
| 한줄평                                          |
| 당신의 인생 영화는 무엇입니까                             |
| 영화 평점                                        |
| 영화 좋아요                                       |
| 회원가입 시 관심장르 체크박스                             |
| 댓글 좋아요                                       |
| 영화 위시리스트                                     |
| 영화 싫어요 시 그와 비슷한 장르 안보이게 하기                   |
| 댓글 필터(최신순, 좋아요순)                             |
| Youtube trailer 가져오기(모달 or 호버) (Youtube API) |
| 영화 저장(인생 영화)                                 |
| 메인영화 크기 제일 크게 만들기 (스크롤 시) (모바일용)             |
| 대댓글                                          |

### 1. 장고 생성

- 가상환경 만들기
  
  python -m venv venv

- 가상환경 실행하기
  
  source/Scripts/activate

- django 버전 설치
  
  pip install django==3.2.13

requirements.txt

```
Django==3.2.13
django-allauth==0.50.0
django-cors-headers==3.13.0
djangorestframework==3.14.0
```

- 가상환경에 package 설정하기
  
  pip install -r requirements.txt

- 패키지 목록 업데이트
  
  pip freeze > requirements.txt

- 프로젝트 생성
  
  django-admin final_pjt (프로젝트이름)

- movies, accounts 앱 생성
  
  python manage.py startapp movies
  
  python manage.py startapp acccount

- 서버 실행
  
  python manage.py runserver

- admin 계정 생성
  
  python manage.py createsuperuser

### 2. API 사용

- Tmdbs API 사용 
  
  https://www.sagein.net/703
  
  ```
  api key : d500a17c48b8de4c2a44437c4ede454e
  api 읽기 엑세스 토큰 : eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNTAwYTE3YzQ4YjhkZTRjMmE0NDQzN2M0ZWRlNDU0ZSIsInN1YiI6IjYzNzMyMGM1ZWQyYWMyMDA5MWYyNjVlMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NNiiwLK6nsOfJQ_JI4dXkSVfLDkAtFg42kUTwvimhN4
  ```

- 사용 section : MOVIES/Get Top Rated
  
  https://developers.themoviedb.org/3/movies/get-top-rated-movies
  
  ![스크린샷 2022-11-16 오전 11.40.05](/Users/poser/Library/Application Support/typora-user-images/스크린샷 2022-11-16 오전 11.40.05.png)
  
  *page는 임의로 1로 지정
  
  ```
  https://api.themoviedb.org/3/movie/top_rated?api_key=d500a17c48b8de4c2a44437c4ede454e&language=ko-KR&page=1
  ```

### 3. Python으로 API 받아오기

- 패키지 설치

```
pip install request
pip freeze > requirements.txt //requirements.txt에 넣어주기
```

- Movies app 내에 API 요청 데이터 받아오는 python 파일 생성(get_movie_data.py)
- tdmb API로부터 받아온 영화 정보 Json화

```python
# movies > get_movie_data.py

#######################################
#
# by. 규형 (22/11/16)
# tdmb API로부터 영화 정보 Json화
# 
#######################################

def tmdb_movie_data():
    # tmdb에서 받아온 Top Rated Movie api 주소와 설정들
    API_KEY = 'd500a17c48b8de4c2a44437c4ede454e'
    LANGUAGE = 'ko-KR'
    PAGE = 1
    API_URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language={LANGUAGE}&page={PAGE}'

    # requestData 변수에 요청값 저장, json으로 변경
    requestData = requests.get(API_URL)
    jsonData = requestData.json()
```

### 4.  Json 파일로 생성 및 저장하기

```python
#######################################
#
# by. 규형 (22/11/16)
# Json화 한 영화 정보 중 원하는 필드만 선택해 fixture 폴더 내 json 파일로 생성
# 
#######################################

def movie_data_save(movie_data):
    movie_list = []
    for movie in movie_data:
        movie_dict = {
            "model" : "movies.movie",
            "pk" : movie.get("id"),
            "fields" : {
                "title" : movie.get("title"),
                "poster_path" : movie.get("poster_path")
            }
        }
        movie_list.append(movie_dict)

    with open('fixtures/movie_data.json', 'a', encoding='utf-8') as file:
        json.dump(movie_list, file, indent='\t', ensure_ascii=False)

movie_data = tmdb_movie_data()
movie_data_save(movie_data)
```

- 추가 설명
  
  - python에서 with문 사용에 대한 참고자료 :  https://wikidocs.net/26
  
  - python에서 Json file 다루는 방법 : https://jsikim1.tistory.com/221
  
  - Python Json dump 한글 깨짐 방법 : https://jsikim1.tistory.com/222

- terminal 내에서 python 코드 실행
  
  ```
  python movies/get_movie_data.py
  ```

- 실행 결과 - fixtures에 movie_data.json 파일 생성됨

![스크린샷 2022-11-16 오후 3.48.31](/Users/poser/Desktop/스크린샷 2022-11-16 오후 3.48.31.png)

### 5. Json 파일 DB에 저장

- Movies > models.py 에 클래스 작성
  
  ```python
  # movies > models.py
  
  from django.db import models
  
  # Create your models here.
  
  class Movie(models.Model):
      title = models.TextField()
      poster_path = models.TextField()
  ```

- Migrate 실행 후 DB 생성 확인
  
  ```
  # terminal
  
  python managy.py makemigrations
  
  python managy.py migrate
  ```
  
  ![스크린샷 2022-11-16 오후 4.12.46](/Users/poser/Library/Application Support/typora-user-images/스크린샷 2022-11-16 오후 4.12.46.png)

## 재현 참고 코드

```python
import csv
import json
import requests
from urllib import parse
from collections import OrderedDict

#######################################
#
# by. 재현 (22/11/13)
# args ->
# platform_list   = 플랫폼별 임의 정수값
# 
#######################################

platform_list = {
    '영화관': 10000,
    'Netflix': 20000,
    'wavve': 30000,
    'Watcha': 40000,
    'Disney Plus': 50000,
    'Netflix basic with Ads': 60000,
    }

#######################################
#
# by. 재현 (22/11/13)
# write_platforms_to_JSON = JSON 파일에 platforms 작성
#
#######################################
def write_platforms_to_JSON():
    platform_json_list = []
    for platform, platform_pk in platform_list.items():
        data = {
            'model': 'movies.platform',
            'pk': platform_pk,
            'fields': {
                'name': platform
            }
        }
        platform_json_list.append(data)
    with open('platforms.json', 'w', encoding='utf-8') as make_file:
        json.dump(platform_json_list, make_file, ensure_ascii=False, indent='\t')
#######################################
#
# by. 재현 (22/11/13)
# write_genres_list_to_JSON = JSON 파일에 TMDB genre API 를 이용한 genre List 작성
# args ->
# API_KEY    = TMDB API KEY
# LANGUAGE   = 검색 결과 언어
#######################################
def write_genres_list_to_JSON():
    API_KEY = '47da6481215fc08ab41d67bda3a0fef1'
    LANGUAGE = 'ko-KR'
    URI = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language={LANGUAGE}' 
    res = requests.get(URI)
    res_json = res.json()
    res_result = res_json['genres']

    genre_json_list = []
    for result in res_result:
        pk   = result['id']
        name = result['name']
        data = {
            'model': 'movies.genre',
            'pk': pk,
            'fields': {
                'name': name,
            }
        }
        genre_json_list.append(data)
    with open('genres.json', 'w', encoding='utf-8') as make_file:
        json.dump(genre_json_list, make_file, ensure_ascii=False, indent='\t')
#######################################
#
# by. 재현 (22/11/13)
# get_movies_detail_info = TMDB Search API - Response Data 를 활용한 영화별 디테일 정보 Json화
# args ->
# API_KEY    = TMDB API KEY
# LANGUAGE   = 검색 결과 언어
# PAGE       = 검색 결과를 출력한 페이지 개수
# QUERY      = 검색할 영화 제목(encoding)
# URI        = Search API URI
# res_json   = Response Data
# res_result = Response Data Results(:List)
# 분기점       = 한국 영화 타이틀과 일치했을 때 기준으로 잘 못된 정보 수집 방지를 위해 출시 연도(오차 범위 1)까지 비교
#######################################
def get_movies_detail_info(movie_kr_title, release_year):
    API_KEY = '47da6481215fc08ab41d67bda3a0fef1'
    LANGUAGE = 'ko-KR'
    PAGE = 1
    QUERY = parse.quote(movie_kr_title)
    URI = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language={LANGUAGE}&page={PAGE}&query={QUERY}' 
    res = requests.get(URI)
    res_json = res.json()
    res_result = res_json['results']
    if res_result:
        for result in res_result:
            movie_kr_title = ('').join(movie_kr_title.split(' '))
            res_kr_title = ('').join(result['title'].split(' '))
            try:
                res_release_year = int((result['release_date'])[:4])
            except:
                continue
            if movie_kr_title == res_kr_title and (release_year == res_release_year or release_year - 1 == res_release_year or release_year + 1 == res_release_year):
                file_data = OrderedDict()
                file_data['title']          = result['title']
                file_data['original_title'] = result['original_title']
                file_data['id']             = result['id']
                file_data['genres']         = result['genre_ids']
                file_data['popularity']     = result['popularity']
                file_data['poster_path']    = 'https://image.tmdb.org/t/p/w500' + result['poster_path']
                file_data['release_date']   = result['release_date']
                file_data['vote_average']   = result['vote_average']
                file_data['vote_count']     = result['vote_count']
                file_data['overview']       = result['overview']
                return file_data

#######################################
#
# by. 재현 (22/11/14)
# get_showing_movies_on_streaming_flatform = Crawling 을 이용한 현재 플랫폼에서 상영 중인 Movie List CSV File
#
#######################################
def get_showing_movies_on_streaming_platform():
        csv_file = open('./crawling_movie_list.csv', 'r', encoding='utf-8')
        movie_list = csv.reader(csv_file)
        return movie_list

#######################################
#
# by. 재현 (22/11/14)
# get_showing_movies_on_cinema = KOBIS API 를 이용한 현재 상영 중 영화 리스트 반환
# args ->
# API_KEY     = KOBIS API KEY
# TARGETDATE  = 조회하고자 하는 날짜
# ITEMPERPAGE = 결과 ROW 개수 지정
# URI         = KOBIS 주간/주말 박스오피스 API
# WEEK        = 조회하고자 하는 날짜의 주간
#######################################
def get_showing_movies_on_cinema():
    API_KEY = '356db2a7eca85c30689f8de561ed0b61'
    TARGETDATE = '20221112'
    ITEMPERPAGE = 10
    WEEK = 0 
    URI = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={API_KEY}&targetDt={TARGETDATE}&itemPerPage={ITEMPERPAGE}&weekGb={WEEK}'
    res = requests.get(URI)
    res_json = res.json()

    box_office_result = res_json['boxOfficeResult']
    weekly_boxoffice_list = box_office_result['weeklyBoxOfficeList']

    showing_movie_list = []
    for showing_movie in weekly_boxoffice_list:
        movie_title = showing_movie['movieNm']
        release_year = (showing_movie['openDt'])[:4]
        streaming_platforms = platform_list['영화관']
        movie_info = [movie_title, release_year, streaming_platforms]
        showing_movie_list.append(movie_info)
    return showing_movie_list

#######################################
#
# by. 재현 (22/11/13)
# dump_movies_to_JSON = 영화 정보가 저장된 리스트를 순회하며 TMDB API 응답 값을 JSON 파일에 DUMP
# args ->
# movie_list = 영화 정보가 담긴 리스트
# file_data = TMDB API 호출을 통해 저장된 영화별 디테일 정보를 JSON화 한 변수
# 분기점 = Movie_list 가 스트리밍 플랫폼 또는 영화관 인지 구분하기 위한 변수
# 
#######################################
def dump_movies_to_JSON(movie_list):
    movie_json_list = []
    for movie_info in movie_list:
        movie_kr_title = movie_info[0]
        release_year = int(movie_info[1])
        file_data = get_movies_detail_info(movie_kr_title, release_year)
        if file_data:
            data = {
                'model': 'movies.movie',
                'fields': file_data
            }
            movie_json_list.append(data)

            new_data = OrderedDict()
            new_data['movie'] = file_data['id']

            streaming_platforms_count = int(movie_info[2])
            if len(movie_info) != 3:
                streaming_platforms = list(map(int, movie_info[3:3 + streaming_platforms_count]))
                streaming_platforms_urls = movie_info[3 + streaming_platforms_count:]
                for platform, url in zip(streaming_platforms, streaming_platforms_urls):
                    new_data['platform'] = platform
                    new_data['url'] = url
                    platforms_data = {
                        'model': 'movies.streamingplatformurl',
                        'fields': new_data,
                    }
                    movie_json_list.append(platforms_data)
            else:
                cinema = platform_list['영화관']
                new_data['platform'] = cinema
                new_data['url'] = '/'
                platforms_data = {
                    'model': 'movies.streamingplatformurl',
                    'fields': new_data,
                }
                movie_json_list.append(platforms_data)

    with open('movies.json', 'a', encoding='utf-8') as make_file:
        json.dump(movie_json_list, make_file, ensure_ascii=False, indent='\t')

def dump_movies_trailer_to_JSON():
    with open('./movies.json', 'r') as json_file:
        movie_json_list = json.load(json_file)

    movie_trailer_json_list = []
    for movie_info in movie_json_list:
        try:
            movie = movie_info['fields']
            movie_id = movie['id']
            API_KEY = '47da6481215fc08ab41d67bda3a0fef1'
            MOVIE_ID = movie_id
            LANGUAGE = 'ko-KR'
            URI = f'https://api.themoviedb.org/3/movie/{MOVIE_ID}/videos?api_key={API_KEY}&language={LANGUAGE}'
            res = requests.get(URI)
            res_json = res.json()
            res_result = res_json['results']

            for result in res_result:
                movie_key = result['key']
                youtube_trailer_url = f'https://www.youtube.com/watch?v={movie_key}'

                fields = OrderedDict()
                fields['movie'] = movie_id
                fields['url'] = youtube_trailer_url

                data = {
                    'model': 'movies.trailer',
                    'fields': fields,
                }
                movie_trailer_json_list.append(data)
        except:
            pass

    with open('movies_trailer.json', 'a', encoding='utf-8') as make_file:
        json.dump(movie_trailer_json_list, make_file, ensure_ascii=False, indent='\t')
```
