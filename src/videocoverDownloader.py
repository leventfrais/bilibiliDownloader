import os
import requests


def download_video_cover(cover_url, main_title):
    save_path = os.path.join("downloads", main_title, main_title + ".jpg")
    response = requests.get(cover_url)

    if response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, "wb") as f:
            f.write(response.content)
    else:
        print(f"图片下载失败，状态码: {response.status_code}")
