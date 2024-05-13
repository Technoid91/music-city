import cloudinary.uploader

def fetch_youtube_thumbnail(video_url):
    try:
        video_id = video_url.split('/')[-1].split('?')[0]
        youtube_thumbnail_url = f'https://img.youtube.com/vi/{video_id}/mqdefault.jpg'
        response = cloudinary.uploader.upload(youtube_thumbnail_url)  # Загрузка изображения на Cloudinary
        if 'secure_url' in response:
            return response['secure_url']  # Возвращаем URL обложки на Cloudinary
        print('[ ! ] cannot fetch Youtube thumbnail')
        return None
    except Exception as e:
        print(f"Error fetching YouTube thumbnail: {e}")
        return None