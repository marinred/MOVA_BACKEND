import os
import sys
import csv
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mova.settings")
django.setup()

from webtoon.models import Webtoon

naver_webtoon_path = './csv/naver_webtoon.csv'
naver_webtoon_finish_path = './csv/naver_webtoon_finish.csv'
kakao_webtoon_path = './csv/kakao_webtoon_weekday.csv'
kakao_webtoon_finish_path = './csv/kakao_webtoon_finished.csv'

def insert_naver_webtoon():
    with open(naver_webtoon_path, encoding='utf-8-sig') as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            if row[0]:
                platform = row[6]
                title = row[1]
                author = row[2]
                image_url = row[8]
                summary = row[5]
                genre = row[4]
                day_of_the_week = row[3]
                webtoon_link = row[7]
                Webtoon.objects.create(
                    platform = platform,
                    title = title,
                    author=author,
                    image_url=image_url,
                    summary=summary,
                    genre=genre,
                    day_of_the_week=day_of_the_week,
                    webtoon_link= webtoon_link
                )
                
def insert_naver_webtoon_finish():
    with open(naver_webtoon_finish_path, encoding='utf-8-sig') as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            if row[0]:
                platform = row[6]
                title = row[1]
                author = row[2]
                image_url = row[8]
                summary = row[5]
                genre = row[4]
                day_of_the_week = row[3]
                webtoon_link = row[7]
                Webtoon.objects.create(
                    platform = platform,
                    title = title,
                    author=author,
                    image_url=image_url,
                    summary=summary,
                    genre=genre,
                    day_of_the_week=day_of_the_week,
                    webtoon_link= webtoon_link
                )
def insert_kakao_webtoon():
    with open(kakao_webtoon_path, encoding='utf-8-sig') as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            if row[0]:
                platform = row[6]
                title = row[1]
                author = row[2]
                image_url = row[8]
                summary = row[5]
                genre = row[4]
                day_of_the_week = row[3]
                webtoon_link = row[7]
                Webtoon.objects.create(
                    platform = platform,
                    title = title,
                    author=author,
                    image_url=image_url,
                    summary=summary,
                    genre=genre,
                    day_of_the_week=day_of_the_week,
                    webtoon_link= webtoon_link
                )                              

def insert_kakao_webtoon_finish():
    with open(kakao_webtoon_finish_path, encoding='utf-8-sig') as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            if row[0]:
                platform = row[6]
                title = row[1]
                author = row[2]
                image_url = row[8]
                summary = row[5]
                genre = row[4]
                day_of_the_week = row[3]
                webtoon_link = row[7]
                Webtoon.objects.create(
                    platform = platform,
                    title = title,
                    author=author,
                    image_url=image_url,
                    summary=summary,
                    genre=genre,
                    day_of_the_week=day_of_the_week,
                    webtoon_link= webtoon_link
                )           
insert_naver_webtoon()
insert_naver_webtoon_finish()
insert_kakao_webtoon()
insert_kakao_webtoon_finish()