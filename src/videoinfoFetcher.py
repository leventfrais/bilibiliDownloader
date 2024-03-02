import requests
from datetime import timedelta


def format_duration(seconds):
    # timedelta 规范格式
    duration = timedelta(seconds=seconds)
    return str(duration)


def fetch_video_info(bvid, pnum):
    # 伪造 headers 防止 412
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
        "Cache - Control": "max - age = 0"
    }
    params = {
        'bvid': bvid,
    }

    # 视频播放信息  参考b站api接口 https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/info.md
    api_video_info = "https://api.bilibili.com/x/web-interface/view"
    response = requests.get(api_video_info, params=params, headers=headers)

    if response.status_code == 200:
        json_data = response.json()

        # 处理错误信息
        if json_data.get('code', 0) != 0:
            error_code = json_data.get('code', '未知代码')
            error_message = json_data.get('message', '未知错误')
            if error_code == -400:
                print(f"视频详情请求失败，错误代码 {error_code}: 请求错误 - {error_message}")
            elif error_code == -404:
                print(f"视频详情请求失败，错误代码 {error_code}: 未找到视频 - {error_message}")
            else:
                print(f"视频详情请求失败，未知错误代码 {error_code}: {error_message}")

        else:
            item = json_data.get('data', [])
            cover_url = item.get('pic')
            title = item.get('title')

            # 遍历 data 即 所有分p
            for page_info in item.get('pages', []):
                if 'cid' in page_info and page_info['page'] == pnum:
                    cvid = page_info['cid']
                    page = page_info['page']
                    part = page_info.get('part', '')
                    duration = page_info.get('duration', 0)
                    #print(f"cid: {cvid}")
                    #print(f"集数: {page}")
                    #print(f"分p标题: {part}")
                    #print(f"时长: {duration}\n")

                    formatted_duration = format_duration(duration)
                    return title, cover_url, page, part, formatted_duration, cvid
    else:
        print(f"访问失败: {response.status_code}")


if __name__ == "__main__":
    # 未分p 娜娜米
    # bid="BV1TN411Y72a"
    # 分p php
    bid = "BV1xt42187mT"
    pnumb = 1
    cid = fetch_video_info(bid, pnumb)
