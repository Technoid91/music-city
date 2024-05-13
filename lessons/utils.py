import requests
from django.core.files.base import ContentFile
from lessons.models import Lesson


def fetch_youtube_thumbnail(video_url):
    video_id = video_url.split('/')[-1].split('?')[0]
    youtube_thumbnail_url = f'https://img.youtube.com/vi/{video_id}/mqdefault.jpg'
    response = requests.get(youtube_thumbnail_url)
    if response.status_code == 200:
        return ContentFile(response.content)
    print('[ ! ] cannot fetch Youtube thumbnail')
    return None