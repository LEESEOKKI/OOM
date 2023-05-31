from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import json
import requests
import time
from bs4 import BeautifulSoup

# chromedriver의 위치 지정


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    return driver


#######################################
#
# by. 규형 (22/11/17)
# [영화관입장권 통합전산망(KOBIS)] 일별 박스오피스 데이터 크롤링
# https://www.kobis.or.kr/kobis/business/stat/boxs/findDailyBoxOfficeList.do
#
#######################################

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


# 함수 실행
driver = set_chrome_driver()
kobis_boxoffice_data(driver)

#######################################
#
# by. 규형 (22/11/17)
# 박스오피스 1-10위 포스터, 요약 정보 가져오기
#
#######################################


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


# 함수 실행
driver = set_chrome_driver()
kobis_boxoffice_movie_detail(driver)
