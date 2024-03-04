import os
import requests
from tqdm import tqdm


def download_video_cover(cover_url, main_title):
    save_path = os.path.join("downloads", main_title, main_title + ".jpg")
    response = requests.get(cover_url)
    cover_size = int(response.headers["Content-Length"])
    chunk_size = 8192

    if response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with tqdm(
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
                miniters=1,
                desc=f"正在下载 {main_title} 的封面",
                total=cover_size,
        ) as prog_bar:
            with open(save_path, "wb") as f:
                for data in response.iter_content(chunk_size=chunk_size):
                    f.write(data)
                    prog_bar.update(len(data))

        prog_bar.close()
    else:
        print(f"图片下载失败，状态码: {response.status_code}")


if __name__ == '__main__':
    URL = "http://i1.hdslb.com/bfs/storyff/n220111a211hlfswzpa3aq2qknjkq938_firsti.jpg"
    TITLE = "阿梓录播210309 删减 - 2.2(Av204608834,P2)_Trim"
    download_video_cover(URL, TITLE)
