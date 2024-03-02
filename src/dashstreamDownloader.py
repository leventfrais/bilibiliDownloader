import os
import requests
import shutil


def download_dash_stream(bvid, video_url, video_main_title, video_part_title, file_format):
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

    if response.status_code == 200:
        downloads_path = "downloads"  # 保存至上一级目录的downloads文件夹
        os.makedirs(downloads_path, exist_ok=True)

        file_name = os.path.join(downloads_path, video_folder_title, video_part_title)
        os.makedirs(os.path.dirname(file_name), exist_ok=True)

        with open(file_name, 'wb') as video_file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, video_file)

    else:
        print(f"下载失败！ 错误代码：{response.status_code}")


if __name__ == "__main__":
    video_stream_url = "https://xy61x159x92x169xy.mcdn.bilivideo.cn:4483/upgcxcode/86/78/1215747886/1215747886-1-30077.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1709296140&gen=playurlv2&os=mcdn&oi=1964815572&trid=000025fccfc3e5d042a9813ea05fbfd1b268u&mid=1396266597&platform=pc&upsig=a7172d2fb9086a9f0e873707c5526e07&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003101&bvc=vod&nettype=0&orderid=0,3&buvid=C777E8D5-34FD-0269-9045-45B12623AD9937889infoc&build=0&f=u_0_0&agrr=1&bw=158453&logo=A0000001"
    # audio_stream_url = "https://cn-jsnt-ct-01-10.bilivideo.com/upgcxcode/86/78/1215747886/1215747886-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1709297178&gen=playurlv2&os=bcache&oi=1964815572&trid=000057e372763b434f749e23e0371fb13446u&mid=1396266597&platform=pc&upsig=d213f62b814ec1a501fd9207800cbbb7&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&cdnid=4280&bvc=vod&nettype=0&orderid=0,3&buvid=C777E8D5-34FD-0269-9045-45B12623AD9937889infoc&build=0&f=u_0_0&agrr=1&bw=21446&logo=80000000"
    bid = "BV1xt42187mT"
    main_title = "30077 超爽七海娜娜米鬼叫合集.mp4"
    part_title = "30077 超爽七海娜娜米鬼叫合集 p1.mp4"
    download_dash_stream(bid, video_stream_url, main_title, part_title, ".m4s")
