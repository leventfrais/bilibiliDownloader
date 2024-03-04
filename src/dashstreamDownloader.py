import os
import requests
from tqdm import tqdm


def download_dash_stream(bvid, video_url, video_main_title, video_part_title, file_format, page, stream_format):
    video_folder_title = video_main_title
    video_part_title += file_format
    fake_referer = "https://www.bilibili.com/video/"
    fake_referer += bvid
    session = requests.Session()
    headers = {
        "Referer": fake_referer,
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Dest": "video"
    }
    response = session.get(video_url, headers=headers, stream=True)
    stream_size = int(response.headers.get('content-length', 0))

    if response.status_code == 200:
        downloads_path = "downloads"  # 保存至上一级目录的downloads文件夹
        os.makedirs(downloads_path, exist_ok=True)

        file_name = os.path.join(downloads_path, video_folder_title, video_part_title)
        os.makedirs(os.path.dirname(file_name), exist_ok=True)

        if stream_format == 1:
            desc_str = f"正在下载视频 P{page} {video_main_title}"
        elif stream_format == 2:
            desc_str = f"正在下载音频 P{page} {video_main_title}"
        else:
            desc_str = f"正在下载 P{page} {video_main_title}"

        with tqdm(
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            miniters=1,
            desc=desc_str,
            total=stream_size,
        ) as prog_bar:
            with open(file_name, 'wb') as video_file, prog_bar:
                response.raw.decode_content = True
                for data in response.iter_content(chunk_size=1024):
                    video_file.write(data)
                    prog_bar.update(len(data))

                prog_bar.close()

    else:
        print(f"下载失败！ 错误代码：{response.status_code}")


if __name__ == "__main__":
    video_stream_url = "https://xy61x147x214x66xy.mcdn.bilivideo.cn:4483/upgcxcode/04/44/1389144404/1389144404-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1709530748&gen=playurlv2&os=mcdn&oi=1851196896&trid=0000b259cd71c6764ea78524e02f00cebb10u&mid=1396266597&platform=pc&upsig=bd0e246e11f77ac4f3d4f4f8346243fa&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=50000580&bvc=vod&nettype=0&orderid=0,3&buvid=C777E8D5-34FD-0269-9045-45B12623AD9937889infoc&build=0&f=u_0_0&agrr=0&bw=211308&logo=A0020000"
    # audio_stream_url = "https://cn-jsnt-ct-01-10.bilivideo.com/upgcxcode/86/78/1215747886/1215747886-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1709297178&gen=playurlv2&os=bcache&oi=1964815572&trid=000057e372763b434f749e23e0371fb13446u&mid=1396266597&platform=pc&upsig=d213f62b814ec1a501fd9207800cbbb7&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&cdnid=4280&bvc=vod&nettype=0&orderid=0,3&buvid=C777E8D5-34FD-0269-9045-45B12623AD9937889infoc&build=0&f=u_0_0&agrr=1&bw=21446&logo=80000000"
    bid = "BV1xt42187mT"
    main_title = "阿梓唱绝不认输"
    part_title = "绝不认输 p1"
    vid_page = 1
    download_dash_stream(bid, video_stream_url, main_title, part_title, ".m4s", vid_page)
