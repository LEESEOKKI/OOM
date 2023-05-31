# final_pjt

# 구미 2반

# 이석기, 이경완, 황규형

<<<<<<< HEAD:final_pjt.md




=======
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
---

# 역할 분담

## **FE, BE** **구분** **없이** **기능** **위주** **분담**

- 이석기(팀장)

- - Community 게시글 CRUD 구현
  - Movie Detail 페이지 구현

- 이경완

- - 회원가입, 로그인/아웃 기능 구현
  - 메인페이지 구현
  - Recommend 페이지 구현

- 황규형

- - Movie Data 수집(API 데이터 요청 함수 구현, 크롤링 함수 구현)
  - Movie Detail 페이지 댓글 CRD 구현

---

# 서비스 대표 기능

- 박스오피스 일일 관객 수 데이터 통해 의사결정에 도움 

- - 타겟은 영화 매니아는 아닌 일반 소비자
  - API와 크롤링 통한 데이터 수집

- 영화 상세정보 페이지 내 한줄평 작성 및 삭제로 영화에 대한 의견 공유 가능

- 커뮤니티 페이지 내 게시글 작성을 통해 다른 의견 공유

---

# 영화 추천 알고리즘

<<<<<<< HEAD:final_pjt.md


=======
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
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
<<<<<<< HEAD:final_pjt.md
     
     실행되도록 설정.



=======
    
     실행되도록 설정.

>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
---

# 데이터베이스 모델링 (ERD)

<<<<<<< HEAD:final_pjt.md
![image-20221125003510937](/Users/poser/Library/Application Support/typora-user-images/image-20221125003510937.png)
=======
![img](https://lab.ssafy.com/seokki0328/final-pjt/-/blob/master/%EB%93%9C%EB%A1%9C%EC%9A%B0%EB%8B%B7%EC%95%84%EC%9D%B4%EC%98%A4.png)
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md

---

# 실제 구현 정도

- 메인 페이지
- 랜덤 페이지
- 커뮤니티 페이지
- 로그인, 로그아웃
- 커뮤니티 게시글 CRUD
- 홈페이지 댓글 CRUD

---

# 느낀점

1학기에 걸쳐 python의 framework인 django와 vue를 사용해 zero-base부터Full-stack 과정을 구현해보면서 하나의 웹 페이지가 어떻게 만들어지는지를 알 수 있었다. 더구나 혼자서 하는 것이 아닌 팀원과 함께 하면서 각 역할을 분배해 기능을 구현하면서 맡은 부분에 대한 책임감과 함께 해낼 수 있다는 긍적적인 사고를 키울 수 있었다. 처음 시작하면서 Brain storming을 통해 다양한 아이디어들을 효과성과 구현가능성을 점수로 측정해 나열하였고 많은 목표 서비스를 구현해보자 하였으나 생각보다 어렵고 오류 투성이로 해결하다보니 목표 기능을 모두 구현하지 못해 아쉽지만 주어진 시간이 더 많았다면 다양한 기능을 만들어 편리함을 더 제공해줄 수 있었을 것이다. 하지만 만족한다. 우리조 만의 기능을 만들어냈다는 것에 !

이 프로젝트를 경험삼아 이후 있을 프로젝트, 입사 후 프로젝트에서도 더욱 시너지를 낼 수 있도록 할 것이다.

- Git 협업 미숙

- - 숙지 필요

- Django 와 Vue 사용 미숙으로 기획에 비해 실제 구현 정도가 미숙

- - FE, BE 구분 없이 기능 단위로 분담하다보니 숙지하는데 시간이 더 걸린 것 같음
  - 사용 기술 숙지 필요
  - 사용자 인증관련 기술 매우 미흡

<<<<<<< HEAD:final_pjt.md


=======
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
---

# api 통해 영화 데이터 가져오기

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
# back-enf > movies > get_data > tdmb_api.py

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
            # 가져오고자 하는 필드와 데이 지정   
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

- Migrate 실행 후 DB 생성 
  
  ```
  # terminal
  
  python managy.py makemigrations
  
  python managy.py migrate
  
  python managy.py loaddata 파일명.json
  ```

## 

## 크롤링 통해 데이터 가져오기

### 0. KOBIS(영화관입장권통합전산망) 일별 박스오피스 상위권 순위 10개 영화 크롤링.

- https://www.kobis.or.kr/kobis/business/stat/boxs/findDailyBoxOfficeList.do

### 1.  크롤링 위한 chromeDriver 및  라이브러리(selenium, request, BeautifulSoup) 설치

```python
# back-enf > movies > get_data > kobis.crawling.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import json
import requests
import time
from bs4 import BeautifulSoup
.
.
.
```

### 2. 함수 구성 및 실행

- chromedriver의 위치 지정
  
  ```python
  # back-enf > movies > get_data > kobis.crawling.py
  def set_chrome_driver():
   chrome_options = webdriver.ChromeOptions()
   driver = webdriver.Chrome(service=Service(
   ChromeDriverManager().install()), options=chrome_options)
   return driver
  ```

- 데이터 크롤링 함수 생성

```python
# back-enf > movies > get_data > kobis.crawling.py

def kobis_boxoffice_data(driver):

    # 암묵적으로 웹 자원 로드 위해 3초 기다림
    driver.implicitly_wait(3)

    # url에 접근
    driver.get(
        'https://www.kobis.or.kr/kobis/business/stat/boxs/findDailyBoxOfficeList.do')

    # 데이터 수집
    movie_data = []

    for order in range(1, 11, 1):
        data_dict = {
            "model": "movies.kobis",
            "pk": order,
            "fields": {
                "order": driver.find_element(By.XPATH, f'//*[@id="tbody_0"]/tr[{order}]/td[{1}]').text,
                "name": driver.find_element(By.XPATH, f'//*[@id="tbody_0"]/tr[{order}]/td[{2}]').text,
                "open_data": driver.find_element(By.XPATH, f'//*[@id="tbody_0"]/tr[{order}]/td[{3}]').text,
                "sales": driver.find_element(By.XPATH, f'//*[@id="tbody_0"]/tr[{order}]/td[{4}]').text,
                "sales_per": driver.find_element(By.XPATH, f'//*[@id="tbody_0"]/tr[{order}]/td[{5}]').text,
                "sales_variation": driver.find_element(By.XPATH, f'//*[@id="tbody_0"]/tr[{order}]/td[{6}]').text,
                "sales_total": driver.find_element(By.XPATH, f'//*[@id="tbody_0"]/tr[{order}]/td[{7}]').text,
                "spectators": driver.find_element(By.XPATH, f'//*[@id="tbody_0"]/tr[{order}]/td[{8}]').text,
                "spectators_variation": driver.find_element(By.XPATH, f'//*[@id="tbody_0"]/tr[{order}]/td[{9}]').text,
                "spectators_total": driver.find_element(By.XPATH, f'//*[@id="tbody_0"]/tr[{order}]/td[{10}]').text,
                "screen": driver.find_element(By.XPATH, f'//*[@id="tbody_0"]/tr[{order}]/td[{11}]').text,
                "screen_time": driver.find_element(By.XPATH, f'//*[@id="tbody_0"]/tr[{order}]/td[{12}]').text,
            }
        }
        movie_data.append(data_dict)

    with open('fixtures/kobis_data.json', 'a', encoding='utf-8') as file:
        json.dump(movie_data, file, indent='\t', ensure_ascii=False)
```

<<<<<<< HEAD:final_pjt.md


=======
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
- 고화질 포스터 img URL과 영화 상세정보 위한 크롤링 함수 생성

  ```python
  # back-enf > movies > get_data > kobis.crawling.py
  
  def kobis_boxoffice_movie_detail(driver):
      # 암묵적으로 웹 자원 로드 위해 3초 기다림
      driver.implicitly_wait(3)
  
      # url에 접근
      req = requests.get(
          'https://www.kobis.or.kr/kobis/business/stat/boxs/findDailyBoxOfficeList.do')
      soup = BeautifulSoup(req.text, 'html.parser')
  
      driver.get(
          'https://www.kobis.or.kr/kobis/business/stat/boxs/findDailyBoxOfficeList.do')
  
      # 데이터 수집
      detail_data_list = []
  
      for order in range(1, 11, 1):
          # 클릭하여 상세 정보 들어가기
          driver.find_element(
              By.XPATH, f'//*[@id="tbody_0"]/tr[{order}]/td[2]/span[1]/a').click()
  
          time.sleep(1)
  
          poster_path = driver.find_element(
              By.CSS_SELECTOR, '.cont_tab > div.item_tab > div.ovf > a')
          POSTER_URL = poster_path.get_attribute('href')
  
          detail_data = driver.find_element(
              By.CSS_SELECTOR, '.cont_tab > div.item_tab > div.ovf > dl.ovf > dd:nth-child(8)')
          MOVIE_DETAIL = detail_data.text
  
          # 상세 정보 저장하기
          data_dict = {
              "model": "movies.detail",
              "pk": order,
              "fields": {
                  "poster_path": POSTER_URL,
                  "movie_detail": MOVIE_DETAIL,
              }
          }
          detail_data_list.append(data_dict)
  
          # 상세 정보 나가기
          driver.find_element(
              By.XPATH, '/html/body/div[3]/div[1]/div[1]/a[2]/span').click()
  
      with open('fixtures/kobis_detail.json', 'a', encoding='utf-8') as file:
          json.dump(detail_data_list, file, indent='\t', ensure_ascii=False)
  ```

<<<<<<< HEAD:final_pjt.md

=======
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
- 함수 실행

```python
# 함수 실행
driver = set_chrome_driver()
kobis_boxoffice_data(driver)

driver = set_chrome_driver()
kobis_boxoffice_movie_detail(driver)
```

<<<<<<< HEAD:final_pjt.md




---

=======
---

>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
# 메인 페이지

Movie API 를 AJAX로 요청 후 데이터를 JSON 방식으로 front-end에 전달

store/index.js

```javascript
// state
movies: [],
kobises: [],


// mutations
GET_MOVIES(state, movies){
  state.movies = movies
},
GET_KOBISES(state, kobises){
  state.kobises = kobises
},


// actions
getMovies(context){
  axios({
    method: 'get',
    url: `${API_URL}/api/v1/movielist/`,
  })
    .then((res) => {
      // console.log(res, context)
      context.commit('GET_MOVIES', res.data)
    })
    .catch((err) => {console.log(err)})
},
getKobises(context){
  axios({
    method: 'get',
    url: `${API_URL}/api/v1/kobislist/`,
  })
    .then((res) => {
      // console.log(res, context)
      context.commit('GET_KOBISES', res.data)
    })
    .catch((err) => {console.log(err)})
},
```

Movies, Kobises 는 각 영화 사이트를 의미하며 API를 받아오고 main page와 recommend page의 영화를 보여주기 위해 구별. (main page = Kobises, recommend = Movies)

store/index.js에 'get' method로 받아 url을 back-end 서버('http://127.0.0.1:8000')를 API_URL 변수로 지정 후 나머지 주소(json)를 입력해준다. 두 영화 모두 응답하게 되면 mutation으로 보내 state에 영화를 저장한다.

Main page (HomeView.vue)에 Movie 영화 카드방식으로 출력 후 cols 설정 및 백그라운드 그라데이션 설정

Main page의 영화 클릭 시 Detail page(MovieDetailView.vue)로 이동 기능 구현

HomeView.vue

```javascript
<template>
    <NowMovie/>
</template>


<script>
import NowMovie from '@/components/NowMovie'

export default {
    name: 'HomeView',
    components: {
        NowMovie
    },
    created(){
        this.getKobises()
    },
    methods: {
        getKobises(){
            this.$store.dispatch('getKobises')
        }
    }
}
</script>
```

HomeView에서는 created 되면 methods 실행되는 정도로만 구현해주고 상세 작업은 NowMovie component에서 해 주기 때문에 tempate에 <NowMovie/> 작성해준다.

NowMovie.vue

```javascript
<template>
    <div class="py-5">
      <div class="container">
          <div class="row row-cols-1 row-cols-sm-2 ">
              <NowMovieItem class="col my-2"
                  v-for="detail in details"
                  :key="detail.id"
                  :detail="detail"
              />
          </div>
      </div>
    </div>
</template>

<script>
import NowMovieItem from '@/components/NowMovieItem'

export default {
    name: 'NowMovie',
    components: {
      NowMovieItem,
    },
}
</script>
```

NowMovie에는 영화의 정보를 v-for를 통해 하나씩 불러오는 정도로만 사용할 것이다.

상세 정보는 NowMovieItem component에서 다룰 것이기 때문에 마찬가지로 template에 NowMovieItem을, script에 import, component에 각각 작성해준다.

 NowMovieItem.vue

```javascript
<template>
    <div>
        <b-card no-body class="overflow-hidden" style="max-width: 540px;">
            <b-row no-gutters>
            <b-col md="6">
                <b-card-img
        :src="detail.poster_path"
        @click="toDetail" class="rounded-0">
        </b-card-img>
            </b-col>
            <b-col md="6">
                <b-card-body>
                    <b-card-text>
                        <div id="title">
                            <span v-for="(kobis,i) in kobises" :key="i">
                                <div v-if="kobis.id == detail.id" class="card-title">
                                    {{kobis.name.split('\n', 1)[0]}}
                                </div>
                            </span>
                        </div>
                        <hr>
                        <div id="font" >
                            <span v-for="(kobis,i) in kobises" :key="i">
                                <div v-if="kobis.id == detail.id" class="card-title">
                                    어제 관객 수 {{kobis.spectators.split('\n', 1)[0]}}
                                </div>
                            </span>
                        </div>
                        <p>{{detail.movie_detail.split('|',6)[2]}}</p>
                        <p>{{detail.movie_detail.split('|',6)[3].split(' ',2)[1]}}</p>
                        <p>{{detail.movie_detail.split('|',6)[4]}}</p>
                        <p>{{detail.movie_detail.split('|',6)[5]}}</p>
                    </b-card-text>
                </b-card-body>
            </b-col>
            </b-row>
        </b-card>
    </div>
</template>

<script>

export default {
    name: 'NowMovieItem',

    props: {
        detail: Object,
    },
    methods: {
      toDetail(){
        this.$router.push({name: 'MovieDetailView', params: {id: this.detail.id}})
      }
    },
    computed: {
      kobises(){
        return this.$store.state.kobises
      },
    },
}
</script>

<style>
/* b-card{
    position: absolute;
    object-fit: cover;
} */
.imgSize {
    width: 250;
    height: 370;
    object-fit: cover !important;
}
.card-img-top {
  height: 15em;
  object-fit: scale-down;
}
#title{
    font-size: 26px;
    font-weight: bold;
    color: #7F6AF7;
}
#font{
    color: gold;
    font-size: 25px;
    font-weight: bold;
    font-family: sans-serif;
    animation: blink-effect 1s step-end infinite;
}
@keyframes blink-effect {
  50% {
    opacity: 0;
  }
}
</style>
```

NowMovieItem은 본격적인 design과 Movie의 상세정보를 나타내는 page이다.

먼저 computed로 store의 state에 담긴 kobises 영화들을 불러온 뒤 v-for문으로 model에 있는 요소들을 하나씩 꺼내오면서 html에 나타내게 해준다.

Movie.poster를 클릭시에는 Detail page로 넘어가게 하기위해 template에 @click="toDetail" 설정해주고 script methods에 this.$router.push({name: 'MovieDetailView', params: {id: this.detail.id}}) 를 적어주어 클릭한 영화의 id 정보와 함께 MovieDetailView 화면으로 넘어가게 설정해준다.

이로써 HomeView(Main page)에 카드정보로 영화를 보여줄 수가 있다.

Detail page의 디자인 구성 및 텍스트 최상위 설정. (UI 기능)

MovieDetailView.vue

```javascript
<template id="no-scroll">
  <div id="no-scroll">
    <img :src="detail?.poster_path" id="back">
      <div style="background: linear-gradient(to left, transparent, rgb(6,6,6)); height: 2750px;">
        <div id="text">
          <span v-for="(kobis,i) in kobises" :key="i">
            <div v-if="(kobis?.id == detail?.id)">
                {{kobis?.name.split('\n', 1)[0]}}
            </div>
          </span>
          <div id="content">
            {{detail?.movie_detail}}
          </div>
          <br>
          <span v-for="(kobis,idx) in kobises" :key="`o-${idx}`">
            <h4 v-if="(kobis?.id == detail?.id)">
                개봉일 : {{kobis?.open_data.split('\n', 1)[0]}}<br><br>
                누적관객수 : {{kobis?.spectators_total.split('\n', 1)[0]}} 명<br><br>
                평점 : 💗{{kobis?.average}}<br><br>
            </h4>
          </span><br>
          <hr>
          <div id="content">상세정보
            <div id="overview">
              <span v-for="(kobis,i) in kobises" :key="i">
                <div v-if="(kobis?.id == detail?.id)">
                    {{kobis?.overview.split('\n', 1)[0]}}
                </div>
              </span>
            </div>
          </div>
        </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'MovieDetailView',
    data(){
        return {
          detail: null,
          kobis: null,
        }
    },
    computed: {
      details(){
        return this.$store.state.details
      },
      kobises(){
        return this.$store.state.kobises
      }
    },
    created(){
      this.getMovieDetail()
    },
    mounted() {
      window.scrollTo(0, 0);
      document.addEventListener('scroll', this.scrollEvents);
    },
    methods: {
      getMovieDetail(){
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/nowlist/${this.$route.params.id}`
        })
         .then(res => {
            this.detail = res.data
          })
          .catch((err) =>{
            console.log(err)
          })
      }
    }
}
</script>

<style>
#back{
  background: linear-gradient(to left, transparent, rgb(6,6,6));
  position: absolute;
  width: 100%;
  z-index: -1;
}
#text{
  color: white;
  position: absolute;
  letter-spacing: 5px;
  font-weight: bold;
  font-size: 60px;
  left: 200px;
  top: 350px;
  right: 200px;
}
#content{
  margin-top: 30px;
  font-size: 30px;
}
#no-scroll {
    overflow: hidden !important
}
hr{
  background: white;
  height: 1px;
  border: 0;
}
#overview{
  margin-top: 50px;
  font-size: 25px;
}
</style>
```

background 배경이 클릭한 영화의 포스터화면이 나오게 설정함과 동시에 그라데이션을 주어 더욱 세련된 느낌을 주었다.

detail 정보를 보여주기 위해 computed로 details와 kobises 정보를 불러오고 detail page가 열릴때 methods를 실행하는 것으로 구현하였다.

template단에서 img :src="detail?.poster_path" 코드로 영화 포스터를 불러오고 style="background: linear-gradient(to left, transparent, rgb(6,6,6)); height: 2750px;" 로 설정하였다.

그리고 그 배경 위로 영화 정보를 text로 나오게 해주었다. 역시나 v-for 문을 사용해 model 요소를 하나씩 가져오면서 출력하는 것으로 만들어주었다.

이렇게 사용하기 위해서 store에서 detail에 대한 axios를 해주어야 한다.

store/index.js

```javascript
// state
details: []


// mutations
GET_DETAILS(state, details){
  state.details = details
}


// actions
getDetails(context){
  axios({
    method: 'get',
    url: `${API_URL}/api/v1/nowlist/`,
  })
    .then((res) => {
      // console.log(res, context)
      context.commit('GET_DETAILS', res.data)
    })
    .catch((err) => {console.log(err)})
}
```

<<<<<<< HEAD:final_pjt.md




=======
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
---

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
<<<<<<< HEAD:final_pjt.md
         
         실행되도록 설정.



=======
    
         실행되도록 설정.

>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
---

# 커뮤니티 페이지

<<<<<<< HEAD:final_pjt.md


=======
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
store에서 앞서 kobises의 영화를 불러온 것과 같은 방식으로 구현해준다.

Community 기능 중 Article(게시판) CRUD 기능을 back-end에서 모델링 한 후 front-end에서 axios로 받아 html로 출력

model

```django
from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

user는 AUTH_USER_MODEL을 사용해 ForeignKey로 설정해주었다. 그리고 게시글의 title, content, created_at(작성일자), updated_at(수정일자)를 요소로 넣어주었다.

serializers

```django
from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
```

Article model을 참고하여 username을 설정한 뒤 restframework로 전달해주기 위해 구현하였다.

urls

```django
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
]
```

article_list 목록을 보여줄 url과 article_detail로 보여줄 url 두 가지 path를 만들어주고 detail path에는 article의 pk 값까지 함께 적어준다.

views

```django
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import ArticleSerializer, ArticleListSerializer
from .models import Article


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):

    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response()

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

먼저 게시글 사용을 인증된 사용자만이 사용할 수 있도록 IsAthenticated를 공통적으로 decoration으로 설정하였다. 

article_list 함수에는 GET과 POST method로 나누어 GET일 때는 작성된 게시글 목록들을 보여주고 POST일 때는 게시글 작성(create)이 되도록 나누어 작성해주었다.

article_detail 함수에는 GET, DELETE, PUT method로 나누어 GET일 때는 게시글의 상세정보를 보여주고 DELETE일 때는 게시글을 삭제, PUT일 때는 게시글을 수정할 수 있도록 나누어 작성하였다.

그리고 이 데이터를 migrations와 migrate를 해준 뒤 front-end에서 html에 나타낼 수 있도록 구현하였다.

store/indes.js

```javascript
// state
articles: []

//mutations
GET_ARTICLES(state, articles){
  state.articles = articles
},
DELETE_ARTICLE(state, article_id){
  state.articles = state.articles.filter((article) => {
    return !(article.id === article_id)
  })
}

// actions
getArticles(context){
  axios({
    method: 'get',
    url: `${API_URL}/api/v1/articles/`,
    headers: {
      Authorization: `Token ${context.state.token}`
    }
  })
    .then(res =>
      context.commit('GET_ARTICLES', res.data)
    )
    .catch(err => console.log(err))
},

updateArticle(context, payload){
  const title = payload.title
  const content = payload.content
  const article_id = payload.article_id
  axios({
    method: 'put',
    url: `${API_URL}/api/v1/articles/${article_id}/`,
    headers: {
      Authorization: `Token ${ context.state.token }`
    },
    data:{
      title,
      content
    }
  })
  .then((res) => {
    console.log(res) 
  })
  .catch((err) => {
    console.log(err)
  })
}
```

axios로 받아오기 때문에 앞에서 사용했던 방식과 동일하게 해주되 인증된 사용자만이 사용가능하기 때문에 action에 headers: {Authorization: `Token ${context.state.token}`}을 추가해준다. 그리고 mutation을 통해 게시글 데이터들을 저장할 articles 리스트를 state에 만들어준다.

단, update는 주의할 것이 있다. method를 put으로 설정해야 하고 title, content, article_id의 변수를 만들어 주어 수정 시 게시글 내용을 그대로 불러오게 설정해야되기 때문에 해당 글의 id 값을 함께 적어주어야 한다.

ArticleCreateView.vue

```javascript
<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="ArticleCreateView">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <button>제출</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleCreateView',
  data() {
    return {
      title: null,
      content: null
    }
  },
  methods: {
   ArticleCreateView() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: {
          title,
          content
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          // console.log(res)
          this.$router.push({name: 'community'})
        })
        .catch(err => console.log(err))
    }
  }
}
</script>
```

게시글 작성(create)에서는 title, content 구성으로 이루어지도록 template 단에 작성해주고 script 단에는 data를 담을 수 있도록 title과 content 변수를 null로 초기화로 잡아주었다.

methods에 if 조건문은 제목이나 내용을 입력하지 않고 작성완료 버튼을 누르면 게시글이 만들어 지지 않도록 설정해 둔 코드이다.

ArticleDetailView.vue

```javascript
<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button @click="deleteArticle">삭제</button>
    <router-link :to="{ name : 'ArticleUpdateView', params : { id : this.article?.id } }">수정</router-link>
    <router-link :to="{ name : 'community' }">뒤로</router-link>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailView',
  data() {
    return {
      article: null
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then((res) => {
        console.log(res.data)
        this.article = res.data
      })
      .catch(err => console.log(err))
    },
    deleteArticle(){
        axios({
          method: 'delete',
          url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((res) => {
            this.article = res.data
            this.$store.commit('DELETE_ARTICLE', this.article.id)
            this.$router.push({ name : 'community'})
        })
        .catch(err => console.log(err))

    }
  }
}
```

Article Detail에는 게시글의 정보를 볼 수 있게 구현하였다. 그 외로 수정할 수 있는 링크와 뒤로 갈 수 있는 링크, 삭제할 수 있는 버튼을 만들어 놓았다. detail 페이지가 생성이 될 때 methods를 동작하고 url에는 게시글의 id 값을 함께 작성해주어야 해당 글의 정보를 볼 수가 있기 때문에 `${API_URL}/api/v1/articles/${this.$route.params.id}/` 이와 같이 작성되어야 한다.

 삭제(delete)시에도 동일하게 작성해준 뒤 삭제 완료 시 push로 community url로 넘어가게 구현하였다.

ArticleUpdateView.vue

```javascript
<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="ArticleUpdateView">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <button @click="ArticleUpdate">완료</button>
      <router-link :to="{name: 'ArticleDetailView' }">뒤로</router-link>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleUpdateView',
  data(){
      return{
      title: null,
      content: null
      }
  },
  created(){
    this.getArticleDetail()
  },
  methods:{
    getArticleDetail() {
      console.log(this.$route.params.id)
      axios({
          method: 'get',
          url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
          headers: {
            Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then((res) => {
          this.title = res.data.title
          this.content = res.data.content
      })
      .catch(err => console.log(err))
    },
    ArticleUpdate(){
      const data = {
        title : this.title,
        content : this.content,
        article_id : this.$route.params.id
      }
      this.$store.dispatch('updateArticle', data)
      this.$router.push({name: 'ArticleDetailView'})
    }
  }
}
</script>
```

update 화면에서는 이전글을 불러오는 기능을 추가하였다. 기본 작성되어 있던 내용을 불러와 수정 후에 다시 ArticleDetail page로 push하게 구현하였다.

이렇게 구조화 한 것을 CommunityView.vue 로 html에 띄우기로 하였다.

CommunityView.vue

```javascript
<template>
  <div>
    커뮤니티 게시판
    <router-link :to="{ name : 'ArticleCreateView'}">
      [글작성란]
    </router-link>
    <hr>
    <ArticleList/>
  </div>

</template>

<script>
import ArticleList from '@/components/ArticleList'

export default {
  name: 'CommunityView',
  components: {
    ArticleList
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({name: 'LogIn'})
      }
    },
  }
}

</script>
```

CommunityView-ArticleList-ArticleListItem 으로 상속관계를 설정하여 구분지어 구현하였다. CommunityView에 접근 하려면 인증 절차를 거쳐야 사용이 가능하게 하였고 Article 형식만 나타내었다.

ArticleList.vue

```javascript
<template>
  <div class="article-list">
    <h3>Article List</h3>
    <ArticleListItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>
```

ArticleList 에는 v-for문으로 computed로 articles 안에 있는 게시글 하나씩 불러오는 형식까지만 구조화 하였다.

ArticleListItme.vue

```javascript
<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p> 작성자 : {{ article.username }}</p>
    <p>{{ article.title }}</p>
    <router-link :to="{ name: 'ArticleDetailView', params: { id: article.id } }">
      [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object
  },
}
</script>
```

<<<<<<< HEAD:final_pjt.md




---

# 회원가입, 로그인, 로그아웃

=======
---

# 회원가입, 로그인, 로그아웃

>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
### 1. accounts 앱 생성

    AbstractUser 함수 활용.

### 2. CORS header 라이브러리 준비

    CORS는 추가 HTTP Header를 사용해 다른 출처의 자원에 접근케 하는 권한 부여.
    $ pip install django-cors-headers
    
    $ pip freeze > requirements.txt
    
    INSTALLED_APPS = [
    
    'corsheaders',
    ]

<<<<<<< HEAD:final_pjt.md

=======
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
​    

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

<<<<<<< HEAD:final_pjt.md




=======
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
---

# 영화 디테일 페이지 내 COMMENT 생성

### 1. Back-end

Django 서버 내 모델 설정 후 특정 url에서 HTTP Response 통해 통신하도록 설정.

- model 설정
<<<<<<< HEAD:final_pjt.md

=======
  
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
  ```python
  # back-end > movies > models.py
  from django.db import models
  from tkinter import CASCADE
  .
  .
  .
  class Comment(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  ```

- views.py 내 댓글 Create, Read, Delete 함수 생성
<<<<<<< HEAD:final_pjt.md

=======
  
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
  ```python
  # back-end > movies > views.py
  from django.shortcuts import get_list_or_404, get_object_or_404
  from rest_framework import status
  from rest_framework.response import Response
  from rest_framework.decorators import api_view
  from .models import Comment
  .
  .
  .
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
  ```

- url 설정
<<<<<<< HEAD:final_pjt.md

=======
  
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
  ```python
  # back-end > movies > urls.py
  from django.urls import path
  from . import views
  .
  .
  .
  
  path('nowlist/<int:detail_id>/comments/', views.comment_create),
  path('<int:detail_id>/comments/', views.get_comment_list),
  path('comments/<int:comment_id>/', views.comment_delete),
  ```

- Serializer 설정
<<<<<<< HEAD:final_pjt.md

=======
  
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
  ```python
   # back-end > movies > serializers.py
  from rest_framework import serializers
  from .models import Comment
  .
  .
  .
  class CommentSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)
  
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('detail',)
  ```

### 2. Front-end

- Vue components에 CommentForm, CommentList, CommentListItem 추가

- CommentForm
<<<<<<< HEAD:final_pjt.md

=======
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
1. input 박스에 내용 작성 후 엔터나, 작성 버튼 클릭 시 createComment methods 실행되도록 함

2. createComment method는 axios통신 통해 django 서버의 views.py의 comment_creat 함수가 실행되는 url로 post요청

3. comment 객체 생성되어 db에 저장됨

4. 위 작업이 끝난 후 새로고침되어 작성된 댓글 표시될수 있도록 함

<<<<<<< HEAD:final_pjt.md


=======
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
```html
<!-- front-end > src > components > CommentForm.vue-->

<template>
  <div>
    <input type="text" class="input-box" placeholder="  한줄평을 작성해주세요  " v-model="commentItem.content" @keyup.enter="createComment">
    <button class="btn btn-primary btn-create" @click="createComment" >   작성   </button>
  </div>
</template>

<script>
import axios from 'axios'



export default {
  name: 'CommentForm',
  data() {
    return {
      commentItem: {
        content: null,
      }
    }
  },
  props: {
    detail: Object,
  }
  ,
  methods: {
    createComment() {
      const commentItemSet = {
        commentItem: this.commentItem,
        detail: this.detail,
      }
      const API_URL = 'http://127.0.0.1:8000'
<<<<<<< HEAD:final_pjt.md
     
=======

>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
      axios({
      method: 'POST',
      url: `${API_URL}/api/v1/nowlist/${commentItemSet.detail.id}/comments/`,
      data: commentItemSet.commentItem,
      })
      .then((res) => {
        console.log(res.data)
        this.$router.go()
        })
      .catch(err => console.log(err))
        this.commentItem.content = null
<<<<<<< HEAD:final_pjt.md
      
=======

>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
    },
    },
  }
</script>

<style>

</style>
<<<<<<< HEAD:final_pjt.md

```

- CommentList

=======
```

- CommentList
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
1. v-for문 통해 CommentListItem들 차례대로 보여줄 수 있도록 함

2. created시 getCommentS methods실행하게 하여 컴포넌트 로드시 바로 댓글들 보이게 함

3. Comment method는 axios통신 통해 django 서버의 views.py의 get_comment_list 함수가 실행되는 url로 get요청

```html
<!-- front-end > src > components > CommentList.vue-->

<template>
  <div>
    <CommentListItem
      v-for="(comment, idx) in comments"
      :key="idx"
      :comment="comment"
      :detail="detail"
    />

  </div> 
</template>

<script>
import axios from 'axios'

import CommentListItem from '@/components/CommentListItem'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentList',
  components: {
    CommentListItem
  },
  data(){   
    return {
        comments : []
    }    
  },
  props: {
    detail: Object
  },
  created(){
    // this.getComments()
  },
  watch:{
    detail(newDetail){
        axios({
        method: 'get',
        url: `${API_URL}/api/v1/${newDetail?.id}/comments/`,
      })
      .then((res) => {
        this.comments = res.data
        // console.log(this.commments)
<<<<<<< HEAD:final_pjt.md
        
=======

>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
      })
      .catch((err) => {console.log(err)})
    }
  },
  methods: {
    getComments(detail){ 
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/${detail?.id}/comments/`,
      })
      .then((res) => {
        this.comments = res.data
        // console.log(this.commments)
      })
      .catch((err) => {console.log(err)})
    }
  },  
}
</script>

<style>

</style>
<<<<<<< HEAD:final_pjt.md

```

- CommentListItem

=======
```

- CommentListItem
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
1. 상위 컴포넌트인 CommentList에서 받아온 'comment'객체의 정보 표시

2. 삭제 버튼 누르면 deleteComment methods 실행되도록 설정

3. deleteComment method는 axios통신 통해 django 서버의 views.py의 comment_delete 함수가 실행되는 url로 delete 요청

4. db내 데이터 삭제 

5. 위 작업이 끝난 후 새로고침되어 삭제된 댓글 없어질 수 있도록 함

```html
<!-- front-end > src > components > CommentListItem.vue-->

<template>
  <div v-if="comment?.detail==detail?.id">
    <span>{{ comment?.content }}</span>  
    <button @click="deleteComment">삭제</button>
  </div>
</template>

<script>

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentListItem',
  props: {
    comment: {
      type: Object,
    },
    detail: null 
  },
  data() {
    return {
      commentItem: {
        content: this.comment.content
      },
    }
  },
  methods: {
    deleteComment(){ 
      console.log(this.comment.id)
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/comments/${this.comment?.id}/`,
      })
      .then(() => {
        console.log("delete success")
        this.$router.go()

      })
      .catch((err) => {console.log(err)})
    } 
  },
}
</script>

<style>

</style>
<<<<<<< HEAD:final_pjt.md

```





=======
```

>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
MovieDetailView.vue에 Comment 컴포넌트 추가

```html
<!-- front-end > src > components > MovieDetailView.vue-->


<template id="no-scroll">
  <div id="no-scroll">
    <!-- <div class="main my_bg" v-bind:style="{backgroundImage: 'url('+detail?.poster_path+')'}"> -->
    <img :src="detail?.poster_path" id="back">
      <div style="background: linear-gradient(to left, transparent, rgb(6,6,6)); height: 2750px;">
        <div id="text">
          <span v-for="(kobis,i) in kobises" :key="i">
            <div v-if="(kobis?.id == detail?.id)">
                {{kobis?.name.split('\n', 1)[0]}}
            </div>
          </span>
          <div id="content">
            {{detail?.movie_detail}}
          </div>
          <br>
          <span v-for="(kobis,idx) in kobises" :key="`o-${idx}`">
            <h4 v-if="(kobis?.id == detail?.id)">
                개봉일 : {{kobis?.open_data.split('\n', 1)[0]}}<br><br>
                누적관객수 : {{kobis?.spectators_total.split('\n', 1)[0]}} 명<br><br>
                평점 : 💗{{kobis?.average}}<br><br>
            </h4>
          </span><br>
          <hr>
          <div id="content">상세정보
            <div id="overview">
              <span v-for="(kobis,i) in kobises" :key="i">
                <div v-if="(kobis?.id == detail?.id)">
                    {{kobis?.overview.split('\n', 1)[0]}}
                </div>
              </span>
            </div>
          </div>
          <br>
          <hr>
          <CommentForm
          :detail="detail"
          />
          <CommentList
          :detail="detail"
          /> 
        </div>
    </div>
  </div>
 <!-- </div> -->

</template>

<script>
import CommentForm from '@/components/CommentForm'
import CommentList from '@/components/CommentList'

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'MovieDetailView',
    data(){
        return {
          detail: null,
          kobis: null,
        }
    },
    components: {
      CommentForm,
      CommentList,
    },
    computed: {
      details(){
        return this.$store.state.details
      },
      kobises(){
        return this.$store.state.kobises
      }
    },
    created(){
      this.getMovieDetail()
    },
    mounted() {
      window.scrollTo(0, 0);
      document.addEventListener('scroll', this.scrollEvents);
    },
    methods: {
      getMovieDetail(){
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/nowlist/${this.$route.params.id}`
        })
         .then(res => {
            this.detail = res.data
          })
          .catch((err) =>{
            console.log(err)
          })
      }
    }
}
</script>

<style>
/* .my_bg{
  background: linear-gradient(to left, transparent, mistyrose),
  url(https://img.danawa.com/prod_img/500000/783/445/img/13445783_1.jpg?shrink=330:330&_v=20210714124847);
  background-repeat : no-repeat;
  background-size : cover;
} */
#back{
  background: linear-gradient(to left, transparent, rgb(6,6,6));
  position: absolute;
  width: 100%;
  z-index: -1;
}
#text{
  color: white;
  position: absolute;
  letter-spacing: 5px;
  font-weight: bold;
  font-size: 60px;
  left: 200px;
  top: 350px;
  right: 200px;
}
#content{
  margin-top: 30px;
  font-size: 30px;
}
#no-scroll {
    overflow: hidden !important
}
hr{
  background: white;
  height: 1px;
  border: 0;
}
#overview{
  margin-top: 50px;
  font-size: 25px;
}

</style>
```
<<<<<<< HEAD:final_pjt.md





=======
>>>>>>> 2b02010a9f09f14801000cf8934a427d7d15beef:README_ALL.md
