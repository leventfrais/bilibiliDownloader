import re
from src.argparseConsts import create_parser
from src.dashstreamDownloader import download_dash_stream
from src.dashstreamFetcher import fetch_video_stream
from src.mergeVideo import creat_merge_bat_dir
from src.mergeVideo import merge_media
from src.videocoverDownloader import download_video_cover
from src.videoinfoFetcher import fetch_video_info


def extract_bvid(videourl):
    # 正则表达式 提取 bvid
    pattern = r"/BV(\w+)/"
    match = re.search(pattern, videourl)
    if match:
        return f"BV{match.group(1)}"
    else:
        return None


def extract_p_range(p_str):
    # 正则表达式 提取p数
    pattern = r'(\d+)-(\d+)'
    match = re.match(pattern, p_str)

    # 防止瞎输分p
    if match:
        start_p = int(match.group(1))
        end_p = int(match.group(2))
        return start_p, end_p
    else:
        return 1, 1


if __name__ == '__main__':
    parser = create_parser()
    video_info = parser.parse_args()

    # video_info.partial="1-1"
    # video_info.url="https://www.bilibili.com/video/BV1ea411q7Kc/?spm_id_from=333.337.search-card.all.click&vd_source=4185e8587566e68218bb335345f1630a"

    start_p, end_p = extract_p_range(video_info.partial)
    with open('myCookie.txt', 'r', encoding='utf-8') as file:
        Cookie = file.read().strip()

    for p_num in range(start_p, end_p + 1):
        bvid = extract_bvid(video_info.url)
        video_main_title, video_cover_url, video_page, video_part_title, video_duration, cvid = fetch_video_info(bvid,
                                                                                                                 p_num)
        video_stream_url, video_resolution, video_codemode, video_audio_url = fetch_video_stream(bvid, cvid,
                                                                                                 video_info.quality,
                                                                                                 video_info.code,
                                                                                                 Cookie)
        print(
            f"正在下载: {video_main_title}\n P{video_page} - {video_part_title}\n    bid: {bvid}\n    cid: {cvid}\n    "
            f"分辨率: {video_resolution}\n    视频封面url: {video_cover_url}\n    "
            f"视频时长: {video_duration}")
        video_page = str(video_page)
        if video_info.mode == 1:
            download_dash_stream(bvid, video_stream_url, video_main_title, f"P{video_page}.{video_part_title}", ".m4s",
                                 video_page, 1)
            download_dash_stream(bvid, video_audio_url, video_main_title, f"P{video_page}.{video_part_title}", ".m4a",
                                 video_page, 2)
            if p_num == start_p:
                # 仅第一p 下载封面 和给 bat 导入 cd../ 退回目录
                download_video_cover(video_cover_url, video_main_title)
                creat_merge_bat_dir(video_main_title, video_main_title)
            merge_media(video_main_title, video_part_title, f"P{video_page}.{video_part_title}")
            print(f"P{video_page} - {video_part_title} 音视频混流脚本生成成功!")
        elif video_info.mode == 2:
            download_dash_stream(bvid, video_audio_url, video_main_title, video_page, ".m4a", video_page, 2)
        else:
            download_video_cover(video_cover_url, video_main_title)

    print("下载结束!\n")
