import requests
import json

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
    PAGE = 2
    API_URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language={LANGUAGE}&page={PAGE}'

    # requestData 변수에 요청값 저장, json으로 변경
    request_data = requests.get(API_URL)
    json_data = request_data.json()
    movie_data = json_data['results']

    return movie_data


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
            "model": "movies.tmdb",
            "pk": movie.get("id"),
            "fields": {
                "genre_ids": movie.get("genre_ids"),
                "title": movie.get("title"),
                "poster_path": movie.get("poster_path"),
                "vote_average": movie.get("vote_average"),
                "vote_count": movie.get("vote_count"),
                "release_date": movie.get("release_date"),
                "overview": movie.get("overview"),
                
                
            }
        }
        movie_list.append(movie_dict)

    with open('C:/Users/multicampus/Desktop/pjt1122/final_pjt/back-server/fixtures/tdmb_data.json', 'a', encoding='utf-8') as file:
        json.dump(movie_list, file, indent='\t', ensure_ascii=False)


# 함수 실행
movie_data = tmdb_movie_data()
movie_data_save(movie_data)
