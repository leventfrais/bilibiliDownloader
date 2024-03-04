import requests


def fetch_video_stream(bvid, cvid, quality, encode_mode, givenCookie):
    headers = {
        "Sec-Ch-Ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/121.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
        "Cache - Control": "max - age = 0",
        "Cookie": givenCookie
    }
    # fnval 代表DASH格式 api接口参考 https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/videostream_url.md#fnval%E8%A7%86%E9%A2%91%E6%B5%81%E6%A0%BC%E5%BC%8F%E6%A0%87%E8%AF%86
    params = {
        'bvid': bvid,
        'cid': cvid,
        'fnval': 16
    }

    api_video_stream = "https://api.bilibili.com/x/player/playurl"
    response = requests.get(api_video_stream, params=params, headers=headers)
    video_resolution = ""
    video_stream_url = ""
    video_code = ""
    highestAudio_url = ""
    if response.status_code == 200:
        json_data = response.json()

        # 处理错误信息
        if json_data.get('code', 0) != 0:
            error_code = json_data.get('code', '未知代码')
            error_message = json_data.get('message', '未知错误')
            if error_code == -400:
                print(f"视频流请求失败，错误代码 {error_code}: 请求错误 - {error_message}")
            elif error_code == -404:
                print(f"视频流请求失败，错误代码 {error_code}: 未找到视频 - {error_message}")
            else:
                print(f"视频流请求失败，未知错误代码 {error_code}: {error_message}")
        else:
            dash_info = json_data["data"]["dash"]
            video_list = dash_info["video"]
            audio_list = dash_info["audio"]

            isFound = False
            highestAudio = 0
            for video, audio in zip(video_list, audio_list):
                if quality == video['id'] and encode_mode in video['codecs'].lower():
                    isFound = True
                    video_stream_url = video['baseUrl']
                    video_resolution = f"{video['width']} * {video['height']}"
                    video_code = video['codecs']
                    # print(f"视频 ID: {video['id']}")
                    # print(f"基础流 URL: {video_stream_url}")
                    # print(f"分辨率: {video_resolution}")
                    # print(f"编码方式: {video_code}\n")

                if highestAudio <= audio['id']:
                    highestAudio = audio['id']
                    highestAudio_url = audio['baseUrl']

            if not isFound:
                print("未找到清晰度，请重新确定清晰度代码 已为你重新获取最高质量流( -h 获取帮助)")
                print(" (须知: 未登录b站账号的情况下最高只能请求480p 如需更高质量请使用Cookie下载)")
                for video, audio in zip(video_list, audio_list):
                    if encode_mode in video['codecs'].lower():
                        video_stream_url = video['baseUrl']
                        video_resolution = f"{video['width']} * {video['height']}"
                        video_code = video['codecs']
                        # print(f"视频 ID: {video['id']}")
                        # print(f"基础流 URL: {video_stream_url}")
                        # print(f"分辨率: {video_resolution}")
                        # print(f"编码方式: {video_code}\n")

            return video_stream_url, video_resolution, video_code, highestAudio_url

    else:
        print(f"访问失败: {response.status_code}")


if __name__ == "__main__":
    bid = "BV1xt42187mT"
    cid = 1439673055
    quality = 80
    encode_mode = "hev"
    givenCookie = "123"
    streamurl = fetch_video_stream(bid, cid, quality, encode_mode, givenCookie)
